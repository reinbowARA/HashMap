from HashMap import Hashtable


if __name__ == "__main__":
     capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa')
    ]
hashtable = Hashtable(capitals)
print(hashtable)
print(f"The capital of Italy is {hashtable.get_value('Italy')}")