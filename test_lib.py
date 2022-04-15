from Module import Person, Wizard, HealthPotion

def test_Person_name():
    value = Person('James')
    excepted_result = 'James'
    assert value.name == excepted_result


def test_Person_life():
    value = Person('James')
    excepted_result = 100
    result = value.life_points
    assert excepted_result == result


def test_Person_a_life():
    james = Person('James')
    excepted_result = False
    result = james.is_dead()
    assert excepted_result == result


def test_Person_hit_Person():
    attacker = Person('James')
    defender = Person('Bond')
    attacker.hit(defender)
    excepted_result = 90
    result = defender.get_life_points()
    assert excepted_result == result


def test_Person_hit_low():
    attacker = Person('James')
    defender = Person('Bond')
    for i in range(0, 10):
        attacker.hit(defender)
    excepted_result = 0
    result = defender.get_life_points()
    assert excepted_result == result


def test_Wizard_hit_Person():
    attacker = Wizard('James')
    defender = Person('Bond')
    attacker.hit(defender)
    excepted_result = 85
    result = defender.get_life_points()
    assert excepted_result == result


def test_Person_hit_Wizard():
    attacker = Person('James')
    defender = Wizard('Bond')
    attacker.hit(defender)
    excepted_result = 70
    result = defender.get_life_points()
    assert excepted_result == result


def test_Person_hit_Person_dead():
    attacker = Person('James')
    defender = Person('Bond')
    for i in range(0, 10):
        attacker.hit(defender)
    excepted_result = True
    result = defender.is_dead()
    assert excepted_result == result


def test_Person_dead():
    defender = Person('James')
    defender.life_points = 0
    excepted_result = True
    result = defender.is_dead()
    assert excepted_result == result


def test_gained_life_points_30():
    james = Person('James')
    james.gained_life_points(30)
    result = james.life_points
    excepted_result = 130
    assert excepted_result == result


def test_gained_life_points_health_potion_on_Person():
    james = Person('James')
    life_points_before = james.get_life_points()
    popo = HealthPotion()
    life_given = popo.get_given_life_points()
    popo.was_used_by(james)
    result = james.life_points
    excepted_result = life_points_before + life_given
    assert result == excepted_result


def test_gained_life_points_health_potion_on_Wizard():
    james = Wizard('James')
    life_points_before = james.get_life_points()
    popo = HealthPotion()
    life_given = popo.get_given_life_points()
    popo.was_used_by(james)
    result = james.life_points
    excepted_result = life_points_before + life_given
    assert result == excepted_result

# test_gained_life_points_health_potion_on_Wizard()
