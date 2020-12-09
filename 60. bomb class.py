class Bomb():
    '''Simulate a bomb that goes *Boom* after a specified amount of waiting.
    '''
    def __init__(self, fuse_length: int) -> None:
        self._time_remaining = fuse_length
        self._num_ticks = 0

    def wait(self, wait_time: int) -> str:   # Technically, str or None
        self._num_ticks = min(self._time_remaining, wait_time)
        output = None
        if self._time_remaining > 0 and self._time_remaining <= wait_time:
            output = repr(self) + ' *Boom*'
            self._num_ticks = 0
        self._time_remaining = self._time_remaining - self._num_ticks
        return output

    def __str__(self) -> str:
        return "It's a bomb!"
    
    def __repr__(self) -> str:
        return 'Tick ...' * self._num_ticks
