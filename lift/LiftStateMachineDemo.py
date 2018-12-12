

import StateMachineReceipe
from random import randint

# input names
INPUT_FROM_IN_LIFT = range(0, 9)
DEFAULT_FLOOR = 0

# state names
IDLE_STATE = 'on_floor_state'
ON_MOVE_STATE_UP = 'moving_up_state'
ON_MOVE_STATE_DOWN = 'moving_down_state'
STATE_PREPARATION = 'preparation_to_move_state'

class StateStayOnFloor(StateMachineReceipe.State):
    def __init__(self, init_state):
        super(StateStayOnFloor, self).__init__(init_state)

    def run(self):
        print('i dont need to move')

    def next(self, input):
        if (input == INPUT_FROM_IN_LIFT):
            return states[STATE_PREPARATION]
        return self


class StatePreparation(StateMachineReceipe.State):
    def __init__(self):
        super(StatePreparation, self).__init__(STATE_PREPARATION)

    def run(self):
        print('Preparing to move')

    def check_floor(self):
        return current_floor

    def next(self, input):
        if(input > current_floor):
            return states[ON_MOVE_STATE_UP]
        if (input < current_floor):
            return states[ON_MOVE_STATE_DOWN]
        else:
            return self


class StateMovingUp(StateMachineReceipe.State):
    def __init__(self):
        super(StateMovingUp, self).__init__(ON_MOVE_STATE_UP)

    def run(self):
        print('I need to shit ....')

    def next(self, input):
        if (input == StatePreparation.check_floor()):
            return states[STATE_PREPARATION]
        return self


class StateMovingDown(StateMachineReceipe.State):
    def __init__(self):
        super(StateMovingDown, self).__init__(ON_MOVE_STATE_DOWN)

    def run(self):
        print('I am shitting ....')

    def next(self, input):
        if (input == StatePreparation.check_floor()):
            return states[STATE_PREPARATION]
        return self


states = {STATE_PREPARATION : StatePreparation(),
          ON_MOVE_STATE_UP: StateMovingUp(),
          ON_MOVE_STATE_DOWN: StateMovingDown()}


def main():
    init_state = states[IDLE_STATE]
    sm = StateStayOnFloor(init_state)

    # at the moment , predefine all the inputs, later we try something else.
    inputs = [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
    sm.run_states(inputs)
    print('Done - am at state: {}'.format(sm._current_state))

if __name__ == "__main__":
    main()