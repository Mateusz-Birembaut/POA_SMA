class_name Env extends Node2D


@export_range(1, 20)
var number_student: int

@onready var desk = %Desk

var student_scene := preload("res://assets/scene/student2.tscn")
@onready var prof := %Prof

var agents : Array[Agent]

func _ready() -> void:
	desk.position = Vector2i(get_window().size.x/2-150, 100)
	prof.position = Vector2i(get_window().size.x/2 - 25, get_window().size.y/2 - 25)
	#agents.append(prof)
	for i in number_student:
		var new_student := student_scene.instantiate()
		new_student.position = Vector2i(100, 0)
		add_child(new_student)
		agents.append(new_student)


func _process(delta: float) -> void:
	pass

func get_agents() -> Array[Agent]:
	return agents
