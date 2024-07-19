import random
import time
import script


class Play:
    def __init__(self):
        self.health_points = 100
        self.exploration_points = 0
        self.exploration_time = 100
        self.exo_species = False
        self.death_cluster = False
        self.toxicology = False
        self.symptoms = False
        self.mother_list = script.MOTHER_LIST

    def loop_story(self):
        """Goes through the story beats and following questions of the game"""
        if self.mother_list[4] is not None:
            for element in self.mother_list[4]:
                print(element)  # Prints the story beat
                time.sleep(1)  # Pauses between lines for 1 second

        if self.mother_list[4] is script.H05:
            print(f"Your chance of survival is currently at {self.health_points}%.")
        elif self.mother_list[4] is script.H06:
            print(f"You have gathered a total of {self.exploration_points} exploration points.\n")

        # Following if/else test the position/condition of the script to modify the list to exclude what's
        # already been used
        if self.mother_list[5] is not None:
            # Asks the next question in the story and modifies the list to exclude what's already been used
            self.mother_list = self.mother_list[int(input(self.mother_list[5])) + 5]
        elif self.mother_list[0] is False and self.mother_list[7] is None:
            self.mother_list = self.mother_list[6]
        elif self.mother_list[0] is False and self.mother_list[5] is None and self.mother_list[7] is not None:
            if self.mother_list[4] is script.H8:
                if self.exo_species is True:
                    self.mother_list = self.mother_list[6]
                else:
                    self.mother_list = self.mother_list[7]
            elif self.mother_list[4] is script.H6:
                if self.death_cluster is True:
                    self.mother_list = self.mother_list[6]
                else:
                    self.mother_list = self.mother_list[7]
            elif self.mother_list[4] is script.H19:
                if self.toxicology is True:
                    self.mother_list = self.mother_list[6]
                else:
                    self.mother_list = self.mother_list[7]
            elif self.health_points > 5:
                self.mother_list = self.mother_list[6]
            else:
                self.mother_list = self.mother_list[7]

    def stats_update(self):
        """Checks if there are updates to be done to the health, exploration and time stats, and modifies them."""
        if self.mother_list[1] is not None:
            # Updates the health_points with the corresponding value in the list
            self.health_points -= random.randint(0, int(self.mother_list[1]))
        if self.mother_list[2] is not None:
            # Updates the exploration_points with the corresponding value in the list
            self.exploration_points += int(self.mother_list[2])
        if self.mother_list[3] is not None:
            # Updates the exploration_time with the corresponding value in the list
            self.exploration_time -= int(self.mother_list[3])

    def check_health(self):
        """Checks if the player has died and prints the last story beat before the game over"""
        if self.health_points <= 0:

            for item in self.mother_list[4]:
                print(item)  # Prints the game over sequence of the game
                time.sleep(1)  # Pauses between lines for 2 seconds
            print("\nERROR!")
            print(f"Your chance of survival is currently at {self.health_points}%.")
            print("It seems your journey has come to a fatal end.")
            print("Not to worry, Exo-planetary Commanding Officer Julieta foresaw this outcome.")
            print("Initiating Temporal Reset protocol. Please stand by.")
            for j in range(5, 100, +20):
                print(f"{j}%")
                time.sleep(2)
            print("Protocol loaded.")
            print("May your mission find its successful end.")
            return True
        elif self.health_points <= 5:
            for item in self.mother_list[4]:
                print(item)
                time.sleep(1)
            print("\nWARNING!")
            print(f"Your chance of survival is currently at {self.health_points}%.")
            print("Initiating Emergency Extraction protocol. Please stand by.")
            for j in range(5, 100, +20):
                print(f"{j}%")
                time.sleep(2)
            print("Protocol loaded.")
            print("Please remember that upon release from the Medical Bay, you are to report to your "
                  "commanding officer.")
            print("May your next mission find you better prepared.")
            return True
        else:
            return False

    def check_time(self):
        """Checks if the player has run out of time and prints the last story beat before the game over"""
        if self.exploration_time <= 10:
            if self.mother_list[4] is not None:
                for item in self.mother_list[4]:
                    print(item)
                    time.sleep(1)  # Pauses between lines for 2 seconds# Prints the game over sequence of the game
            print("\nWARNING!")
            print(f"Your exploration window has reached the allotted time for Evacuation.")
            print("Initiating Extraction protocol. Please stand by.")
            for j in range(5, 100, +20):
                print(f"{j}%")
                time.sleep(2)
            print("Protocol loaded.")
            print("You may revisit your mission once the danger has passed.")
            return True
        else:
            return False

    def go_home(self):
        """Checks if the player selected the 'go home' option in end-game and
        displays the given protocol"""
        if self.mother_list[4] is script.H062:
            for item in self.mother_list[4]:
                print(item)
                time.sleep(1)
            print("You have activated the Homecoming Protocol.")
            print("Please stand by.")
            for j in range(5, 100, +20):
                print(f"{j}%")
                time.sleep(2)
            print("Protocol loaded.")
            print("Exo-planetary Commanding Officer Julieta will be awaiting your report.")
            print("Please remember to pay a visit to the Medical Bay for a check-up before the end of the night cycle.")
            return True
        else:
            return False

    def check_end_game(self):
        """Checks if mother_list[0] is True. If it is, then the list is the last
        sequence/story beat in the game, which gets printed"""
        if self.mother_list[0] is True:
            for item in self.mother_list[4]:
                print(item)
                time.sleep(1)  # Pauses between lines for 2 seconds# Prints the last sequence of the game
            return True
        else:
            return False

    def profile_question_check(self):
        """Checks the profile questions` answer to set the self_variable to True if the answer is 1"""
        if self.mother_list[8] is True:
            self.exo_species = True
        if self.mother_list[9] is True:
            self.death_cluster = True
        if self.mother_list[10] is True:
            self.toxicology = True
        if self.mother_list[11] is True:
            self.symptoms = True
