class_name Student extends Agent


enum Strategies { NONE , DODGE }

var collected_candies := 0
var time_since_last_collect := 0.0
var interval: float
var time_since_last_interval := 0.0
var strategie : Strategies


func _ready() -> void:
	super._ready()
	speed = 5000
	var rng = RandomNumberGenerator.new()
	interval = rng.randf_range(5, 20)
	strategie = Strategies.values()[randi() % Strategies.size()]
	if env.DEBUG:
		print(name, " strategie : ", strategie)
		print(name, " interval : ", interval)


func _process(delta: float) -> void:
	if time_since_last_interval >= interval:
		print(name, " passe à l'état LEAVE")
		state = States.LEAVE
		time_since_last_interval = 0

	match state:
		States.WORK:
			time_since_last_interval += delta
		States.LEAVE:
			match strategie:
				Strategies.NONE :
					move_none()
				Strategies.DODGE:
					move_dodge()
					
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

func move_none() -> void :
	look_towards(env.candies.position)
	if (position - env.candies.position).length() <= 60:
		velocity = Vector2()
		print(name, " passe à l'état COLLECT")
		state = States.COLLECT
		
func move_dodge() -> void :
	var direction_away_from_prof = (position - env.prof.position).normalized()
	var distance_away_from_prof = (position - env.prof.position).length()
	var evade_range = 400
	
	if distance_away_from_prof <= evade_range:
		var candies_direction = (env.candies.position - position).normalized()
		var ratio = distance_away_from_prof / evade_range
		var movement_direction = ((1 - ratio) * direction_away_from_prof) + (ratio * candies_direction)
		var movement_position = position + movement_direction
		look_towards(movement_position)
	else:
		look_towards(env.candies.position)
		
	if (position - env.candies.position).length() <= 60:
		velocity = Vector2()
		print(name, " passe à l'état COLLECT")
		state = States.COLLECT

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
