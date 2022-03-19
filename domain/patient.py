class Patient:
    def __init__(self, first, last, cnp, disease):
        '''
        Description: constructor
        :param first:
        :param last:
        :param cnp:
        :param disease:
        '''
        self.__first = first
        self.__last = last
        self.__cnp = cnp
        self.__disease = disease
    def getFirst(self):
        '''
        Description: getter method
        :return: returns the first name
        '''
        return self.__first
    def getLast(self):
        '''
        Description: getter method
        :return: returns the last name
        '''
        return self.__last
    def getCnp(self):
        '''
        Description: getter method
        :return: returns the personal numerical code
        '''
        return self.__cnp
    def getDisease(self):
        '''
        Description: getter method
        :return: returns the disease
        '''
        return self.__disease
    def getAge(self):
        almost_age = (self.__cnp // 10000000000) % 100
        if 21 >= almost_age >= 0:
            year = 2000 + almost_age
        else:
            if almost_age >= 22:
                year = 1900 + almost_age
        age = 2021 - year
        return age
    def setFirst(self,first):
        '''
        Description: setter method
        :param first:
        :return: sets the first name
        '''
        self.__first = first
    def setLast(self,last):
        '''
        Description: setter method
        :param last:
        :return: sets the last name
        '''
        self.__last = last
    def setCnp(self,cnp):
        '''
        Description: setter method
        :param cnp:
        :return: sets the personal numerical code
        '''
        self.__cnp = cnp
    def setDisease(self,disease):
        '''
        Description: setter method
        :param disease:
        :return: sets the disease
        '''
        self.__disease = disease
    def __str__(self):
        '''
        :return: the string representation of a patient
        '''
        return "Patient: " + self.__first + " " + self.__last + ", cnp: " + str(self.__cnp) + ", with disease: " + self.__disease

