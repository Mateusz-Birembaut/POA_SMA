extends Agent


var student_to_chase : Agent


func _ready() -> void:
	super._ready()
	speed = 15000


func _process(delta: float) -> void:
	# if CHASE => se déplacer vers l'eleve plus proche bonbons
		#move_towards()
	# if COMEBACK => se déplacer vers la table
		# direction = tablePosition - position . normalize
		# position = position + direction * speed
	# if WORK => regarder si des élèves s'approche des bonbons

	match state:
		States.WORK:
			check_students()
		States.CHASE:
			look_towards(student_to_chase.position)
			if (position - student_to_chase.position).length() <= 50:
				print(name, " renvoit un élève au travail")
				student_to_chase.send_to_work()
				print(name, " passe à l'état COMEBACK")
				state = States.COMEBACK
		States.COMEBACK:
			look_towards(initial_position)
			if (position - initial_position).length() <= 1:
				velocity = Vector2()
				print(name, " passe à l'état WORK")
				state = States.WORK
			check_students()


func check_students() -> void:
	student_to_chase = null
	var shortest_distance := INF
	var distance : float
	for student in env.students:
		distance = (student.position - env.candies.position).length()
		if distance < 100 and distance < shortest_distance:
			print("student near candies !!!!!")
			shortest_distance = distance
			student_to_chase = student
			print(name, " passe à l'état CHASE")
			state = States.CHASE


func see() -> void:
	# get la position de l'eleve le plus proche des bonbons qui soit parti 

	#if studentPosition != null :
		# state = CHASE
	#else:
		#if position == initial_position :
			#state = WORK
		#else :
			#state = COMEBACK 

	pass


func action() -> void:
	pass
