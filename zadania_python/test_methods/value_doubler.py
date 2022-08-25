class ValueDoubler:

    @staticmethod
    def double_odd_value(value: int):
        if value % 2:
            return value * 2
        return value
