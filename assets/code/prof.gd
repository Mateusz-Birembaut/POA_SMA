extends Agent


@onready var env = get_parent()

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
	
	# si position => déplacer vers l'eleve	= CHASE
	#if studentPosition != null :
		# state = CHASE
	#else:
		
	# sinon =>
		# si deja à la table STATE = WORK 
		# sinon revenir vers la table  STATE = COMEBACK

	pass
