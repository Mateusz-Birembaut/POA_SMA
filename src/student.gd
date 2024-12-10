class_name Student extends Agent


enum Strategies { NONE , DODGE }

var time_since_last_collect := 0.0
var interval: float
var time_since_last_interval := 0.0
var evade_range := 400.0
var prefered_group_size : int
var is_solitary : bool
var strategy : Strategies



func _ready() -> void:
	super._ready()
	speed = 5000
	var rng = RandomNumberGenerator.new()
	interval = rng.randf_range(2, 10)
	is_solitary = randf() < 0.75
	strategy = Strategies.values()[randi() % Strategies.size()]
	prefered_group_size = randi_range(2, 3)
	if env.DEBUG:
		print(name, " strategy : ", strategy)
		print(name, " interval : ", interval)
		print("is solitary : ",is_solitary)
	if strategy == Strategies.NONE :
		sprite.modulate = Color(0, 0, 1) # blue shade
	else :
		sprite.modulate = Color(0, 1, 0) # green shade

func _process(delta: float) -> void:
	if time_since_last_interval >= interval:
		if is_solitary:
			print(name, " passe à l'état READY")
			state = States.READY
			time_since_last_interval = 0
		else :
			print(name, " passe à l'état LEAVE")
			state = States.LEAVE
			time_since_last_interval = 0

	match state:
		States.READY:
			time_since_last_interval += delta
			if(env.get_number_ready_student() >= prefered_group_size):
				env.signal_go()

		States.WORK:
			time_since_last_interval += delta

		States.LEAVE:
			match strategy:
				Strategies.NONE :
					move_none()
				Strategies.DODGE:
					move_dodge()
			if (position - env.candies.position).length() <= 60:
				nav.target_position = Vector2()
				velocity = Vector2()
				print(name, " passe à l'état COLLECT")
				state = States.COLLECT

		States.COMEBACK:
			if (nav.get_final_position() - global_position).length() > 30:
				nav.target_position = initial_position
				look_towards(nav.get_next_path_position())
			else:
				look_towards(initial_position)
			if (position - initial_position).length() <= 5:
				nav.target_position = Vector2()
				velocity = Vector2()
				print(name, " passe à l'état WORK")
				state = States.WORK

		States.COLLECT:
			time_since_last_collect += delta
			if time_since_last_collect >= 5:
				env.update_score()
				print(" prend un bonbon")
				time_since_last_collect = 0


func send_to_work() -> void:
	print(name, " passe à l'état COMEBACK")
	state = States.COMEBACK


func move_none() -> void :
	nav.target_position = env.candies.position
	look_towards(nav.get_next_path_position())


func move_dodge() -> void :
		if env.prof.student_to_chase == self:
			var direction_away_from_prof = (position - env.prof.position).normalized()
			var distance_away_from_prof = (position - env.prof.position).length()
			var distance_from_candies = (position - env.candies.position).length()
			if distance_away_from_prof <= evade_range and distance_from_candies >= 100:
				var candies_direction = (env.candies.position - position).normalized()
				var ratio = distance_away_from_prof / evade_range
				var movement_direction = ((1 - ratio) * direction_away_from_prof) + (ratio * candies_direction)
				var movement_position = position + movement_direction
				look_towards(movement_position)
			else:
				look_towards(env.candies.position)
		else :
			look_towards(env.candies.position)

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
