class_name Menu extends Node2D

@onready var PlayButton: Button = %PlayButton;
@onready var ExitButton: Button = %ExitButton;

@onready var NbSlider: HSlider = %NbSlider;
@onready var NbSliderLabel: Label = %NbSliderLabel;
@onready var SpeedSlider: HSlider = %SpeedSlider;
@onready var SpeedSliderLabel: Label = %SpeedSliderLabel;
@onready var CandySlider: HSlider = %CandySlider;
@onready var CandySliderLabel: Label = %CandySliderLabel;
@onready var MenuBox: VBoxContainer = %MenuBox;

@onready var menu_X = 2 * get_window().size.x / 3 - MenuBox.size.x / 2;
@onready var menu_Y = get_window().size.y / 2 - MenuBox.size.y / 2;

func _ready() -> void:
	
	PlayButton.position = Vector2i(
		get_window().size.x / 3 - 100,
		get_window().size.y / 2 - 50
	);
	PlayButton.pressed.connect(launch);
	
	ExitButton.position = Vector2i(
		get_window().size.x / 3 - 100,
		get_window().size.y / 2 + 50
	);
	ExitButton.pressed.connect(quit);
	
	
	###### MENU ######
	MenuBox.position = Vector2i(
		menu_X,
		menu_Y
	);
	NbSlider.drag_ended.connect(setNbStudents);
	SpeedSlider.drag_ended.connect(setSpeed);
	CandySlider.drag_ended.connect(setCandy);

func _process(_delta: float) -> void:
	pass;

func launch() -> void:
	get_tree().change_scene_to_file("res://src/main.tscn");

func quit() -> void:
	get_tree().quit();

func setNbStudents(value_changed: bool) -> void:
	var s: String = "Nombre d'étudiants: " + str(NbSlider.value);
	NbSliderLabel.text = s;

func setSpeed(value_changed: bool) -> void:
	var s: String = "Vitesse de la maîtresse: " + str(SpeedSlider.value);
	SpeedSliderLabel.text = s;

func setCandy(value_changed: bool) -> void:
	var s: String = "Nombre de bonbons: " + str(CandySlider.value);
	CandySliderLabel.text = s;
