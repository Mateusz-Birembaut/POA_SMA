class_name Student extends Agent


var collected_candies := 0
var time_since_last_collect := 0.0
var interval: float
var time_since_last_interval := 0.0


func _ready() -> void:
	super._ready()
	speed = 10000
	var rng = RandomNumberGenerator.new()
	interval = rng.randf_range(5, 20)
	print(interval)


func _process(delta: float) -> void:
	if time_since_last_interval >= interval:
		print(name, " passe à l'état LEAVE")
		state = States.LEAVE
		time_since_last_interval = 0

	match state:
		States.WORK:
			time_since_last_interval += delta
		States.LEAVE:
			look_towards(env.candies.position)
			if (position - env.candies.position).length() <= 60:
				velocity = Vector2()
				print(name, " passe à l'état COLLECT")
				state = States.COLLECT
		States.COMEBACK:
			look_towards(initial_position)
			if (position - initial_position).length() <= 1:
				velocity = Vector2()
				print(name, " passe à l'état WORK")
				state = States.WORK
		States.COLLECT:
			time_since_last_collect += delta
			if time_since_last_collect >= 1:
				collected_candies += 1
				print(name, " nb bonbons : ", collected_candies)
				time_since_last_collect = 0


func send_to_work() -> void:
	print(name, " passe à l'état COMEBACK")
	state = States.COMEBACK


func see() -> void:
	## get la position de l'eleve le plus proche des bonbons qui soit parti 

	## si position => déplacer vers l'eleve = CHASE
	##if studentPosition != null :
		## state = CHASE
	##else:

	## sinon =>
		## si deja à la table STATE = WORK 
		## sinon revenir vers la table  STATE = COMEBACK

	pass


func action() -> void:
	pass
