
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION_KEY AND_KEY DEFINE_KEY DOMAIN_KEY EFFECT_KEY EQUALITY_KEY EQUALS GOAL_KEY HYPHEN INIT_KEY LPAREN NAME NOT_KEY OBJECTS_KEY PARAMETERS_KEY PRECONDITION_KEY PREDICATES_KEY PROBLEM_KEY REQUIREMENTS_KEY RPAREN STRIPS_KEY TYPES_KEY TYPING_KEY VARIABLEpddl : domain\n            | problemdomain : LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPARENproblem : LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPARENdomain_def : LPAREN DOMAIN_KEY NAME RPARENproblem_def : LPAREN PROBLEM_KEY NAME RPARENobjects_def : LPAREN OBJECTS_KEY typed_constants_lst RPARENinit_def : LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN\n                | LPAREN INIT_KEY ground_predicates_lst RPARENgoal_def : LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPARENrequire_def : LPAREN REQUIREMENTS_KEY require_key_lst RPARENrequire_key_lst : require_key require_key_lst\n                       | require_keyrequire_key : STRIPS_KEY\n                   | EQUALITY_KEY\n                   | TYPING_KEYtypes_def : LPAREN TYPES_KEY names_lst RPARENpredicates_def : LPAREN PREDICATES_KEY predicate_def_lst RPARENpredicate_def_lst : predicate_def predicate_def_lst\n                         | predicate_defpredicate_def : LPAREN NAME typed_variables_lst RPAREN\n                     | LPAREN NAME RPARENaction_def_lst : action_def action_def_lst\n                      | action_defaction_def : LPAREN ACTION_KEY NAME parameters_def action_def_body RPARENparameters_def : PARAMETERS_KEY LPAREN typed_variables_lst RPAREN\n                      | PARAMETERS_KEY LPAREN RPARENaction_def_body : precond_def effects_defprecond_def : PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN\n                   | PRECONDITION_KEY literaleffects_def : EFFECT_KEY LPAREN AND_KEY literals_lst RPAREN\n                   | EFFECT_KEY literalliterals_lst : literal literals_lst\n                    | literalliteral : LPAREN NOT_KEY predicate RPAREN\n               | predicateground_predicates_lst : ground_predicate ground_predicates_lst\n                             | ground_predicatepredicate : LPAREN NAME variables_lst RPAREN\n                 | LPAREN EQUALS VARIABLE VARIABLE RPAREN\n                 | LPAREN NAME RPARENground_predicate : LPAREN NAME constants_lst RPAREN\n                        | LPAREN NAME RPARENtyped_constants_lst : constants_lst HYPHEN type typed_constants_lst\n                           | constants_lst HYPHEN typetyped_variables_lst : variables_lst HYPHEN type typed_variables_lst\n                           | variables_lst HYPHEN typeconstants_lst : constant constants_lst\n                     | constantvariables_lst : VARIABLE variables_lst\n                     | VARIABLEnames_lst : NAME names_lst\n                 | NAMEtype : NAMEconstant : NAME'
    
_lr_action_items = {'RPAREN':([18,19,25,26,27,28,29,35,36,39,40,42,44,46,47,48,51,52,53,57,60,62,64,67,68,72,74,76,77,78,80,81,85,86,87,88,90,91,94,95,96,97,98,99,100,103,105,107,108,110,111,115,118,120,121,124,125,126,128,130,131,132,133,134,135,],[30,31,-16,41,-15,-14,-13,50,-53,56,-24,-12,59,63,-49,-55,-52,66,-20,-23,-38,75,-48,-19,78,-37,86,-54,-45,-22,90,-51,97,-43,98,-44,-21,-50,105,106,108,109,-42,-47,-28,-36,-25,117,118,-46,-32,124,-10,129,-34,-41,132,133,134,-33,135,-39,-35,-31,-40,]),'EQUALS':([104,112,122,127,],[114,114,114,114,]),'NAME':([11,12,22,34,36,47,48,54,55,61,65,71,74,76,77,89,104,112,122,127,],[18,19,36,48,36,48,-55,68,69,74,76,74,48,-54,48,76,115,115,115,115,]),'OBJECTS_KEY':([21,],[34,]),'REQUIREMENTS_KEY':([10,],[17,]),'PREDICATES_KEY':([23,],[37,]),'DEFINE_KEY':([1,],[5,]),'PARAMETERS_KEY':([69,],[83,]),'GOAL_KEY':([43,],[58,]),'DOMAIN_KEY':([7,14,],[11,11,]),'EQUALITY_KEY':([17,25,27,28,29,],[27,-16,-15,-14,27,]),'LPAREN':([0,5,6,8,9,13,16,20,24,30,31,32,37,40,41,45,50,53,58,60,63,66,73,75,78,83,84,86,90,93,98,101,103,105,109,113,116,119,121,124,132,133,135,],[1,7,10,14,15,21,23,33,38,-5,-6,43,54,38,-11,61,-17,54,70,71,-7,-18,71,-9,-22,95,71,-43,-21,104,-42,112,-36,-25,-8,122,127,122,122,-41,-39,-35,-40,]),'VARIABLE':([68,76,81,95,99,114,115,123,],[81,-54,81,81,81,123,81,131,]),'$end':([2,3,4,56,59,],[-1,-2,0,-3,-4,]),'EFFECT_KEY':([92,102,103,124,129,132,133,135,],[101,-30,-36,-41,-29,-39,-35,-40,]),'AND_KEY':([61,70,104,112,],[73,84,113,119,]),'HYPHEN':([47,48,49,64,79,81,91,],[-49,-55,65,-48,89,-51,-50,]),'STRIPS_KEY':([17,25,27,28,29,],[28,-16,-15,-14,28,]),'TYPES_KEY':([15,],[22,]),'ACTION_KEY':([38,],[55,]),'PRECONDITION_KEY':([82,106,117,],[93,-27,-26,]),'PROBLEM_KEY':([7,],[12,]),'NOT_KEY':([104,112,122,],[116,116,116,]),'INIT_KEY':([33,],[45,]),'TYPING_KEY':([17,25,27,28,29,],[25,-16,-15,-14,25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'predicates_def':([16,],[24,]),'literal':([93,101,113,119,121,],[102,111,121,121,121,]),'typed_constants_lst':([34,77,],[46,88,]),'objects_def':([13,],[20,]),'typed_variables_lst':([68,95,99,],[80,107,110,]),'goal_def':([32,],[44,]),'predicate_def':([37,53,],[53,53,]),'ground_predicates_lst':([45,60,73,84,],[62,72,85,96,]),'init_def':([20,],[32,]),'ground_predicate':([45,60,73,84,],[60,60,60,60,]),'type':([65,89,],[77,99,]),'require_key_lst':([17,29,],[26,42,]),'domain':([0,],[2,]),'constants_lst':([34,47,74,77,],[49,64,87,49,]),'names_lst':([22,36,],[35,51,]),'action_def_body':([82,],[94,]),'literals_lst':([113,119,121,],[120,128,130,]),'domain_def':([5,8,],[6,13,]),'parameters_def':([69,],[82,]),'constant':([34,47,74,77,],[47,47,47,47,]),'predicate':([93,101,113,116,119,121,],[103,103,103,126,103,103,]),'require_def':([6,],[9,]),'predicate_def_lst':([37,53,],[52,67,]),'types_def':([9,],[16,]),'effects_def':([92,],[100,]),'precond_def':([82,],[92,]),'action_def_lst':([24,40,],[39,57,]),'variables_lst':([68,81,95,99,115,],[79,91,79,79,125,]),'problem_def':([5,],[8,]),'problem':([0,],[3,]),'pddl':([0,],[4,]),'action_def':([24,40,],[40,40,]),'require_key':([17,29,],[29,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> pddl","S'",1,None,None,None),
  ('pddl -> domain','pddl',1,'p_pddl','parser.py',100),
  ('pddl -> problem','pddl',1,'p_pddl','parser.py',101),
  ('domain -> LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPAREN','domain',8,'p_domain','parser.py',106),
  ('problem -> LPAREN DEFINE_KEY problem_def domain_def objects_def init_def goal_def RPAREN','problem',8,'p_problem','parser.py',111),
  ('domain_def -> LPAREN DOMAIN_KEY NAME RPAREN','domain_def',4,'p_domain_def','parser.py',116),
  ('problem_def -> LPAREN PROBLEM_KEY NAME RPAREN','problem_def',4,'p_problem_def','parser.py',121),
  ('objects_def -> LPAREN OBJECTS_KEY typed_constants_lst RPAREN','objects_def',4,'p_objects_def','parser.py',126),
  ('init_def -> LPAREN INIT_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','init_def',7,'p_init_def','parser.py',131),
  ('init_def -> LPAREN INIT_KEY ground_predicates_lst RPAREN','init_def',4,'p_init_def','parser.py',132),
  ('goal_def -> LPAREN GOAL_KEY LPAREN AND_KEY ground_predicates_lst RPAREN RPAREN','goal_def',7,'p_goal_def','parser.py',140),
  ('require_def -> LPAREN REQUIREMENTS_KEY require_key_lst RPAREN','require_def',4,'p_require_def','parser.py',145),
  ('require_key_lst -> require_key require_key_lst','require_key_lst',2,'p_require_key_lst','parser.py',150),
  ('require_key_lst -> require_key','require_key_lst',1,'p_require_key_lst','parser.py',151),
  ('require_key -> STRIPS_KEY','require_key',1,'p_require_key','parser.py',159),
  ('require_key -> EQUALITY_KEY','require_key',1,'p_require_key','parser.py',160),
  ('require_key -> TYPING_KEY','require_key',1,'p_require_key','parser.py',161),
  ('types_def -> LPAREN TYPES_KEY names_lst RPAREN','types_def',4,'p_types_def','parser.py',166),
  ('predicates_def -> LPAREN PREDICATES_KEY predicate_def_lst RPAREN','predicates_def',4,'p_predicates_def','parser.py',171),
  ('predicate_def_lst -> predicate_def predicate_def_lst','predicate_def_lst',2,'p_predicate_def_lst','parser.py',176),
  ('predicate_def_lst -> predicate_def','predicate_def_lst',1,'p_predicate_def_lst','parser.py',177),
  ('predicate_def -> LPAREN NAME typed_variables_lst RPAREN','predicate_def',4,'p_predicate_def','parser.py',185),
  ('predicate_def -> LPAREN NAME RPAREN','predicate_def',3,'p_predicate_def','parser.py',186),
  ('action_def_lst -> action_def action_def_lst','action_def_lst',2,'p_action_def_lst','parser.py',194),
  ('action_def_lst -> action_def','action_def_lst',1,'p_action_def_lst','parser.py',195),
  ('action_def -> LPAREN ACTION_KEY NAME parameters_def action_def_body RPAREN','action_def',6,'p_action_def','parser.py',203),
  ('parameters_def -> PARAMETERS_KEY LPAREN typed_variables_lst RPAREN','parameters_def',4,'p_parameters_def','parser.py',208),
  ('parameters_def -> PARAMETERS_KEY LPAREN RPAREN','parameters_def',3,'p_parameters_def','parser.py',209),
  ('action_def_body -> precond_def effects_def','action_def_body',2,'p_action_def_body','parser.py',217),
  ('precond_def -> PRECONDITION_KEY LPAREN AND_KEY literals_lst RPAREN','precond_def',5,'p_precond_def','parser.py',222),
  ('precond_def -> PRECONDITION_KEY literal','precond_def',2,'p_precond_def','parser.py',223),
  ('effects_def -> EFFECT_KEY LPAREN AND_KEY literals_lst RPAREN','effects_def',5,'p_effects_def','parser.py',231),
  ('effects_def -> EFFECT_KEY literal','effects_def',2,'p_effects_def','parser.py',232),
  ('literals_lst -> literal literals_lst','literals_lst',2,'p_literals_lst','parser.py',240),
  ('literals_lst -> literal','literals_lst',1,'p_literals_lst','parser.py',241),
  ('literal -> LPAREN NOT_KEY predicate RPAREN','literal',4,'p_literal','parser.py',249),
  ('literal -> predicate','literal',1,'p_literal','parser.py',250),
  ('ground_predicates_lst -> ground_predicate ground_predicates_lst','ground_predicates_lst',2,'p_ground_predicates_lst','parser.py',258),
  ('ground_predicates_lst -> ground_predicate','ground_predicates_lst',1,'p_ground_predicates_lst','parser.py',259),
  ('predicate -> LPAREN NAME variables_lst RPAREN','predicate',4,'p_predicate','parser.py',267),
  ('predicate -> LPAREN EQUALS VARIABLE VARIABLE RPAREN','predicate',5,'p_predicate','parser.py',268),
  ('predicate -> LPAREN NAME RPAREN','predicate',3,'p_predicate','parser.py',269),
  ('ground_predicate -> LPAREN NAME constants_lst RPAREN','ground_predicate',4,'p_ground_predicate','parser.py',279),
  ('ground_predicate -> LPAREN NAME RPAREN','ground_predicate',3,'p_ground_predicate','parser.py',280),
  ('typed_constants_lst -> constants_lst HYPHEN type typed_constants_lst','typed_constants_lst',4,'p_typed_constants_lst','parser.py',288),
  ('typed_constants_lst -> constants_lst HYPHEN type','typed_constants_lst',3,'p_typed_constants_lst','parser.py',289),
  ('typed_variables_lst -> variables_lst HYPHEN type typed_variables_lst','typed_variables_lst',4,'p_typed_variables_lst','parser.py',297),
  ('typed_variables_lst -> variables_lst HYPHEN type','typed_variables_lst',3,'p_typed_variables_lst','parser.py',298),
  ('constants_lst -> constant constants_lst','constants_lst',2,'p_constants_lst','parser.py',306),
  ('constants_lst -> constant','constants_lst',1,'p_constants_lst','parser.py',307),
  ('variables_lst -> VARIABLE variables_lst','variables_lst',2,'p_variables_lst','parser.py',315),
  ('variables_lst -> VARIABLE','variables_lst',1,'p_variables_lst','parser.py',316),
  ('names_lst -> NAME names_lst','names_lst',2,'p_names_lst','parser.py',324),
  ('names_lst -> NAME','names_lst',1,'p_names_lst','parser.py',325),
  ('type -> NAME','type',1,'p_type','parser.py',335),
  ('constant -> NAME','constant',1,'p_constant','parser.py',340),
]
