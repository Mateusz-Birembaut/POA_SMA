extends Agent


func _ready() -> void:
	pass


func _process(delta: float) -> void:
	# if CHASE => se déplacer vers l'eleve plus proche bonbons
		# direction = studentPosition - position . normalize
		# position = position + direction * speed
	# if COMEBACK => se déplacer vers la table
		# direction = tablePosition - position . normalize
		# position = position + direction * speed
	# if WORK => ne rien faire
	
	pass
	
	
	
func see() -> void:
	# get la position de l'eleve le plus proche  des bonbon qui soit parti 
	
	#if studentPosition != null :
		# state = CHASE
	#else:
		#if position == initial_position :
			#state = WORK
		#else :
			#state = COMEBACK 

	pass
