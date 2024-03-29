# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:15:00-21:00 15/May/2017

import numpy
import random
import pylab
import pdb
class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        
        # TODO
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        # TODO
        temp = random.random()
        if temp > self.clearProb:
            return False
        else: return True
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        temp = random.random()
        assert popDensity<1
        if temp < self.maxBirthProb*(1-popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        if temp > self.maxBirthProb*(1-popDensity):     
            raise NoChildException
        # TODO

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses = viruses
        self.maxPop = maxPop
        

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        # TODO 
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        for virus in self.viruses:
            if virus.doesClear():
                self.viruses.remove(virus)
        density = float(self.getTotalPop())/self.maxPop
        print density
        for virus in self.viruses:
            try: self.viruses.append(virus.reproduce(density))
            except NoChildException:
                pass
        return self.getTotalPop()
     
        
            
#       
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    # TODO 
    
    viruses = []
    numbers=[]
    for i in range(100): 
        viruses.append(SimpleVirus(0.05,0.05))
    patient = SimplePatient(viruses,1000)
    
    for i in range(30):
        numbers.append(patient.update())
    pylab.plot(list(range(30)),numbers,label='virurses over time')
    pylab.xlabel('periods')
    pylab.ylabel('numbers of viruses')
    pylab.legend()
    pylab.show()
    
    
#
# PROBLEM 3
#
#problem2()
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        
        
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # TODO
        if self.resistances[drug] is True:
            return True
        else:
            return False
        
            
        
    
        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO
        
        assert popDensity<1
        if activeDrugs != []:
            for drugs in activeDrugs:
                if self.getResistance(drugs)  == False:
                    raise NoChildException
        
        temp = random.random()  
        if temp > self.maxBirthProb*(1-popDensity):
            raise NoChildException
        else:
            resistancedic = self.resistances.copy()
            for drugs in self.resistances.keys():
                temp1 = random.random()
                if temp1 < self.mutProb:
                    resistancedic[drugs] = not self.getResistance(drugs)
                else:
                    resistancedic[drugs] = self.getResistance(drugs)
            return ResistantVirus(self.maxBirthProb, self.clearProb, resistancedic, self.mutProb)
                
        
        
        
        print 'reproduce error'
        
        
        
        
        
        
        
        
        
        
        
            
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO
        return self.drugs
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        sumup = 0
        for virus in self.viruses:
            count = 1
            for drugs in drugResist:
                if virus.getResistance(drugs)== False:
                    count = 0
            sumup += count    
        return sumup
            
        
        

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        for virus in self.viruses:
            if virus.doesClear():
                self.viruses.remove(virus)
        density = float(self.getTotalPop())/self.maxPop
        for virus in self.viruses:
            try: self.viruses.append(virus.reproduce(density, self.getPrescriptions()))
            except NoChildException:
                pass
        return self.getTotalPop()
        

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    viruses=[]
    numbers=[]
    for i in range(100):
        viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False},0.005))
    patient = Patient(viruses,1000)
    for i in range(150):
       numbers.append(patient.update())
    patient.addPrescription('guttagonol')
    for i in range(150):
       numbers.append(patient.update()) 
    pylab.plot(list(range(300)),numbers,label='virurses over time')
    pylab.xlabel('periods')
    pylab.ylabel('numbers of viruses')
    pylab.legend()
    pylab.show()
     
        
        
#problem4()
#
# PROBLEM 5
#
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    # TODO
    numbers=[]
    for patients in range(100):
        viruses=[]
        
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False},0.005))
        patient = Patient(viruses,1000)
        for i in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for i in range(150):
            number = patient.update()
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients of various condition at (150,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()
     
    numbers=[]
    for patients in range(100):
        viruses=[]
        
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False},0.005))
        patient = Patient(viruses,1000)
        for i in range(50):
            patient.update()
        patient.addPrescription('guttagonol')
        for i in range(150):
            number = patient.update()
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients of various condition at (50,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()
     
    numbers=[]
    for patients in range(100):
        viruses=[]
        
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False},0.005))
        patient = Patient(viruses,1000)
        patient.addPrescription('guttagonol')
        for i in range(150):
            number = patient.update()
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients of various condition at(0,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()
     
    numbers=[]
    for patients in range(100):
        viruses=[]
        
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False},0.005))
        patient = Patient(viruses,1000)
        for i in range(300):
            patient.update()
        patient.addPrescription('guttagonol')
        for i in range(150):
            number = patient.update()
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients of various condition at(300,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()
     
#problem5()    
#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO
    numbers=[]
    for patient in range(100):
        viruses=[]
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False,'grimpex':False},0.005))
        patient = Patient(viruses,1000)
        for i in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for i in range(150):
            patient.update()
        patient.addPrescription('grimpex')
        for i in range(150):
            number = patient.update()
            
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients with two medicines(150,150,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()
    
    numbers=[]
    for patient in range(100):
        viruses=[]
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False,'grimpex':False},0.005))
        patient = Patient(viruses,1000)
        for i in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for i in range(100):
            patient.update()
        patient.addPrescription('grimpex')
        for i in range(150):
            number = patient.update()
            
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients with two medicines(150,100,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()
    
    numbers=[]
    for patient in range(100):
        viruses=[]
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False,'grimpex':False},0.005))
        patient = Patient(viruses,1000)
        for i in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for i in range(50):
            patient.update()
        patient.addPrescription('grimpex')
        for i in range(150):
            number = patient.update()
            
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients with two medicines(150,50,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()
    
    numbers=[]
    for patient in range(100):
        viruses=[]
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False,'grimpex':False},0.005))
        patient = Patient(viruses,1000)
        for i in range(150):
            patient.update()
        patient.addPrescription('guttagonol')
        for i in range(1):
            patient.update()
        patient.addPrescription('grimpex')
        for i in range(150):
            number = patient.update()
            
        numbers.append(number)
        
    pylab.hist(numbers,label='number of patients with two medicines(150,0,150)')
    pylab.xlabel('viruses')
    pylab.ylabel('numbers of patients')
    pylab.legend()
    pylab.show()





problem6()

#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    # TODO
     # TODO
    
    for patients in range(1):
        viruses=[]
        numbers=[]
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False,'grimpex':False},0.005))
        numbers=[]
        patient = Patient(viruses,1000)
        for i in range(150):
            numbers.append(patient.update())
        patient.addPrescription('guttagonol')
        for i in range(300):
            numbers.append(patient.update())
        patient.addPrescription('grimpex')
        for i in range(150):
            numbers.append(patient.update())
        pylab.plot(list(range(600)),numbers,label='number of viruses of overtime with two medicine')
        pylab.xlabel('viruses')
        pylab.ylabel('numbers of patients')
        pylab.legend()
        pylab.show()
    for patients in range(1):
        viruses=[]
        numbers=[]
        for i in range(100):
            viruses.append(ResistantVirus(0.1,0.05,{'guttagonol':False,'grimpex':False},0.005))
        numbers=[]
        patient = Patient(viruses,1000)
        for i in range(150):
            numbers.append(patient.update())
        patient.addPrescription('guttagonol')
        patient.addPrescription('grimpex')
        for i in range(150):
            numbers.append(patient.update())
        pylab.plot(list(range(300)),numbers,label='number of viruses of overtime with two medicine')
        pylab.xlabel('viruses')
        pylab.ylabel('numbers of patients')
        pylab.legend()
        pylab.show()
    
#problem7()
