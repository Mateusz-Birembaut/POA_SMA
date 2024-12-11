class_name Student extends Agent


enum Strategies { NONE , DODGE, LURE }

var time_since_last_collect := 0.0
var interval: float
var time_since_last_interval := 0.0
var evade_range := 400.0
var prefered_group_size : int
var is_solitary : bool
var strategy : Strategies
var lure = false


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
		print("ici")
		sprite.modulate = Color(0, 0, 1)
	elif strategy ==  Strategies.LURE:
		sprite.modulate = Color(1, 0, 0)
	else :
		sprite.modulate = Color(0, 1, 0)

func _process(delta: float) -> void:
	if time_since_last_interval >= interval:
		if is_solitary and strategy != Strategies.LURE:
			print(name, " passe à l'état READY")
			state = States.READY
			time_since_last_interval = 0
			
		elif strategy == Strategies.LURE :
			if env.get_lure_ready_student() == 0:
				lure = true
				state = States.READY
			else:
				if lure :
					state = States.LEAVE 
				else :
					if !env.lure_exists():
						lure = true
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
				Strategies.LURE:
					move_lure()
			if (position - env.candies.position).length() <= 50:
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
			env.update_score()
			print(" prend un bonbon")
			state = States.COMEBACK


func send_to_work() -> void:
	lure = false
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

func move_lure() -> void:
	if env.prof.student_to_chase == self:
		var direction_away_from_prof = (position - env.prof.position).normalized()
		var direction_to_candies = (env.candies.position - position).normalized()

		var dot_product = direction_away_from_prof.dot(direction_to_candies)

		if dot_product > 0.5: 
			var perpendicular_direction = Vector2(-direction_to_candies.y, direction_to_candies.x).normalized()
			direction_away_from_prof += perpendicular_direction * 0.5
			direction_away_from_prof = direction_away_from_prof.normalized()
		if lure:
			var distance_from_candies = (position - env.candies.position).length()
			if distance_from_candies <= 100:
				look_towards(env.candies.position) 
			else:
				env.signal_friends_go()
				var movement_position = position + direction_away_from_prof
				look_towards(movement_position)
		else:
			look_towards(env.candies.position) 	
	else:
		if lure :
			var direction_to_candies = (env.candies.position - position).normalized() 
			var direction = position + direction_to_candies*0.1
			look_towards(direction)
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
