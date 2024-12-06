class_name Agent extends Sprite2D

enum States {WORK, CHASE, COMEBACK, LEAVE, COLLECT}

@onready var env = get_parent()
@onready var agent : CharacterBody2D = $Agent
@onready var shape : CollisionShape2D = $Shape

var initial_position : Vector2i
var state : States
var speed : float 


func _ready() -> void:
	pass


func _process(delta: float) -> void:
	pass

func move_towards( _position: Vector2 ) -> void:
	var direction = (_position - position).normalized()
	position += direction * speed
	

func see() -> void:
	pass

func action() -> void:
	pass
