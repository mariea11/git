import web
import Maps

urls = (
	'/game', 'Engine'
	'/index', 'Index'
	'/', 'Index',
	'/Out', 'Out'
	)
	
app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

#A little hack so sessions works with debug mode on
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

    
class Index(object):
	# start the session with starting values then move to engine
	def get(self):
		session.room = maps.START
		web.seeother("/game")

# the game engine, which runs the different commands for the game and starts it   
class Engine(object):
	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.you_died()
			
	def out(self):
		session.room.output = "You quit."
		return render.out()
		
	def POST(self):
		form = web.input(action=None)
		
		if form.action and session.room:
			if '*' in session.room.paths:
				if form.action != session.room.num and form.action not in self.commands:
					session.room.guess -= 1
					session.room.output = "..." % session.room.guess
					if session.room.guess == 0:
						session.room = session.room.go('*')
				elif form.action == session.room.num:
					session.room = session.room.go('x')
			else:
				transition = session.room.go(form.action)
				if transition == None:
					session.room.output = "You cannot do that."
				elif transition != None:
					session.room = transition
				else:
					session.room.output = "Please enter a command."
					
		if form.action in self.commands:
			self.commands[form.action]()
			
		web.seeother('/game')
		
#quits the game	
class Out():
	def GET(self):
		return render.out()
		
if __name__ == '__main__':
	app.run()