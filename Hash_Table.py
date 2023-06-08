class Hash_Table:

    class __Entry:
        
        def __init__(self, key, value):
            self.value = value
            self.key = key
            self.isDeleted = False

    def __init__(self, probing_factor):
        self.__array = [None for _ in range(11)]
        self.__array_len = 11 # Size of array
        self.__length = 0 # Number of items in map
        self.__probing_factor = probing_factor # Linear probing factor 

    def to_array(self): # Actual array 
        return self.__array
    
    def array_length(self): # Length of actual array
        return self.__array_len
    
    def size(self): # Number of items in map 
        return self.__length
    
    def __hash(self, val): # Hash function
        return val % self.__array_len

    def __linear_probe(self, key): # Linear probing function 
        actual_key = key
        key = self.__hash(key) 

        while self.__array[key % self.__array_len] != None: 
            if self.__array[key % self.__array_len].isDeleted == False:
                if self.__array[key % self.__array_len].key == actual_key:
                    raise KeyError
                key += self.__probing_factor 

        return key % self.__array_len 
    
    def insert(self, key, value): # Insert method
        if self.__length == self.__array_len//2: 
            self.__grow()

        new_entry = self.__Entry(key, value) 
        hashed_key = self.__hash(key) 
        
        if self.__array[hashed_key] == None or self.__array[hashed_key].isDeleted == True: # Open spot 
            self.__array[hashed_key] = new_entry
        else: 
            self.__array[self.__linear_probe(key)] = new_entry # Collision
        
        self.__length += 1
        
    def __get_object(self,key): # Get method that returns object 
        hashed_key = self.__hash(key)
        
        for i in range(hashed_key, hashed_key + self.__array_len, self.__probing_factor):
            if self.__array[i] == None:
                raise KeyError
            
            elif self.__array[i % self.__array_len].key == key:
                return self.__array[i % self.__array_len]
            
    def get(self,key): # Returns value associated with key
        return self.__get_object(key).value

    def to_list(self): # Returns the entire maping in the form of a list
        list = []
        for item in self.__array:
            if item != None:
                if item.isDeleted == False:
                    list.append(str(item.key) + ' : ' +  str(item.value))
        return list
        
    def delete(self, key): # Delete method
        self.__get_object(key).isDeleted = True
        self.__length -= 1

    def __is_prime(self, x): # Determines if integer is prime
        prime = True
        for i in range(2, x):
            if (x % i) == 0:
                prime = False
                break
        return prime

    def __re_hash_probe(self, key, array): # Probing function specically for re-hashing
        while array[key % len(array)] != None: 
            key += self.__probing_factor 

        return key % len(array) 
    
    def __re_hash(self, array): # Re-hash
        for item in self.__array:
            if item is not None:
                if item.isDeleted == False:
                    hashed_key = item.key % len(array)
                    if array[hashed_key] == None or array[hashed_key].isDeleted == True: 
                        array[hashed_key] = item
                    else: 
                        array[self.__re_hash_probe(hashed_key, array)] = item
        return array

    def __grow(self): # Doubles the size of the array and finds next prime
        new_len = self.__array_len * 2
        while self.__is_prime(new_len) != True:
            new_len += 1
            
        new_arr = [None for _ in range(new_len)]
        self.__array = self.__re_hash(new_arr)

        self.__array_len = new_len

if __name__ == '__main__': 
    Hash = Hash_Table(2)
    Hash.insert(9315484, 'Sample Name 1')
    Hash.insert(9329582, 'Sample Name 2')
    Hash.insert(9301941, 'Sample Name 3')

    print(Hash.get(9315484))

    print('Items in list:', Hash.to_list())
    print('Length of the array:', Hash.array_length())
    print('Number of items:', Hash.size())