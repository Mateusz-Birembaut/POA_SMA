class_name Env extends Node2D


@export_range(1, 20)
var students := 5

@onready var desk = %Desk
@onready var prof : Agent = %Prof

var student_scene := preload("res://assets/scene/student.tscn")
var agents : Array[Agent]

func _ready() -> void:
	desk.position = Vector2i(get_window().size.x/2-150, 100)

	prof.position = Vector2i(get_window().size.x/2 - 25, get_window().size.y/2 - 25)
	agents.append(prof)

	for i in students:
		var new_student : Agent = student_scene.instantiate()
		add_child(new_student)
		agents.append(new_student)


func _process(delta: float) -> void:
	pass

func get_agents() -> Array[Agent]:
	return agents
