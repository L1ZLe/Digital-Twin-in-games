import random



class GameEntity:

    def __init__(self, entity_id, position=(0, 0), health=100, status="active"):

        self.entity_id = entity_id

        self.position = position

        self.health = health

        self.status = status



    def take_damage(self, damage):

        self.health -= damage

        if self.health <= 0:

            self.status = "inactive"

            print(f"{self.entity_id} defeated!")



class DigitalTwinGameEnvironment:

    def __init__(self):

        self.entities = []



    def add_entity(self, entity):

        self.entities.append(entity)



    def simulate_game_event(self):

        # Simulate a game event (e.g., player interaction, enemy spawn)

        event_type = random.choice(["player_attack", "enemy_spawn"])

        if event_type == "player_attack":

            attacker = random.choice([entity for entity in self.entities if isinstance(entity, Player)])

            target = random.choice([entity for entity in self.entities if isinstance(entity, Enemy) and entity.status == "active"])

            damage = random.randint(10, 20)

            print(f"{attacker.entity_id} attacks {target.entity_id} for {damage} damage!")

            target.take_damage(damage)

        elif event_type == "enemy_spawn":

            new_enemy = Enemy(entity_id=f"Enemy-{len(self.entities)+1}")

            print(f"New enemy spawned: {new_enemy.entity_id}")

            self.add_entity(new_enemy)



class Player(GameEntity):

    def __init__(self, entity_id, position=(0, 0), health=100, status="active"):

        super().__init__(entity_id, position, health, status)



class Enemy(GameEntity):

    def __init__(self, entity_id, position=(random.randint(1, 10), random.randint(1, 10)), health=50, status="active"):

        super().__init__(entity_id, position, health, status)



# Example Usage

player1 = Player(entity_id="Player-1")

enemy1 = Enemy(entity_id="Enemy-1")

game_environment = DigitalTwinGameEnvironment()



game_environment.add_entity(player1)

game_environment.add_entity(enemy1)



for _ in range(5):

    game_environment.simulate_game_event()