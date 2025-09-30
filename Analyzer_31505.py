import numpy as np

class Numpy_array :
    array_choice = 0
    layers = 0
    row_element = 0
    column_element = 0 
    
    @classmethod
    def Array_dimension (cls):
        while True : 

            print("\nSelect the type of array to Create\n")
            print("1. 1D Araay : ")
            print("2. 2D Araay : ")
            print("3. 3D Araay : ")
            print("4. Go Back : ")
            Numpy_array.array_choice = int(input("Enter your choice : "))

            
            if Numpy_array.array_choice == 1 :

                element_list  = list(map(int , input ("Enter the elements for the array separated by : ").split()))
                array = np.array(element_list)
                print(array)
                return array
    
            elif Numpy_array.array_choice == 2 :
                Numpy_array.row_element = int(input ("Enter Number of Rows : "))
                Numpy_array.column_element = int(input("Enter Number of column : "))
                element_list  = list(map(int , input (f"Enter the {Numpy_array.row_element*Numpy_array.column_element} elements for the array separated by space : ").split()))
                array = np.array(element_list).reshape(Numpy_array.row_element,Numpy_array.column_element)
                print(array)
                return array
            
            elif Numpy_array.array_choice == 3:
                Numpy_array.layers = int (input("Enter number of layers : "))
                Numpy_array.row_element = int(input ("Enter Number of Rows : "))
                Numpy_array.column_element = int(input("Enter Number of column : "))
                element_list  = list(map(int , input (f"Enter the {Numpy_array.layers*Numpy_array.row_element*Numpy_array.column_element}  elements for the array separated by space : ").split()))
                array = np.array(element_list).reshape(Numpy_array.layers,Numpy_array.row_element,Numpy_array.column_element)
                print(array) 
                return array

            elif Numpy_array.array_choice == 4 :
                print("Exit the input data maenu :")
                break
            else :
                print("Please Enter your number choice in 1 to 4 : ")

    def __init__(self,array):
        self.array = array
        

    def indexing_slicing (self):
        while True :
            print("\nEnter the operation \n")
            print("1. Indexing ")
            print("2. slicing ")
            print("3. Exit ")
            choice_operation = int (input("Enter yuor choice : "))
            if choice_operation == 1 :
                try:
                    element_number = int(input("Enter the indexing element number  :"))
                    print(self.array[element_number])
                except Exception :
                    print("Invalid index! ")

            elif choice_operation == 2 :
                try :

                    row_number = int(input("Enter the row range (Start) : "))
                    row_number1 = int(input("Enter the row range (end) : "))
                    column_number = int(input("Enter the column range (start) : "))
                    column_number1 = int(input("Enter the column range (end) : "))
                    print(self.array[row_number:row_number1,column_number:column_number1])
                except Exception :
                    print("Invalid slice range! ")
            elif choice_operation == 3 :
                print("Exit the Operation : ")
                break
            else:
                print("Please Enter your number choice in 1 to 3.")

    def new_data (self):

        if Numpy_array.array_choice == 1:
            element_list = list(map(int,input("Enter the elements for the array separated by : ").split()))
            new_array = np.array(element_list)
            print("New array \n",new_array)
            return  new_array
        
        elif Numpy_array.array_choice == 2 :
            Numpy_array.row_element
            Numpy_array.column_element
            element_list = list(map(int,(input(f"Enter the {Numpy_array.row_element*Numpy_array.column_element} elements for the array separated by space : ").split())))
            new_array = np.array(element_list).reshape(Numpy_array.row_element,Numpy_array.column_element)
            print("New Array \n",new_array)
            return new_array

        elif Numpy_array.array_choice == 3 :
            Numpy_array.layers
            Numpy_array.row_element
            Numpy_array.column_element
            element_list = list(map(int, input(f"Enter the {Numpy_array.layers*Numpy_array.row_element*Numpy_array.column_element}  elements for the array separated by space : ").split()))
            new_array = np.array(element_list).reshape(Numpy_array.layers,Numpy_array.row_element,Numpy_array.column_element)
            print(new_array)
            return new_array
        else :
            print("Please Enter the valid data : ")



    def Mathematical_Operation (self):
        while True : 
            print("\nMathematical operation : \n")
            print("1. Addition ")
            print("2. subtraction ")
            print("3. Multiplication ")
            print("4. Division ")
            print("5. Go back ")

            math_operation = int(input ("Enter your choice : "))
            
            if math_operation == 1 :
                math_new_data = self.new_data()
                print("\nOld Array \n", self.array)
                sum_array = np.add(self.array,math_new_data)
                print("\nResult_Array:\n",sum_array)

            elif math_operation == 2 :
                math_new_data = self.new_data()
                print("\nOld Array \n", self.array)
                subtractions = np.subtract(self.array,math_new_data)
                print("\nResult : \n",subtractions)
            
            elif math_operation == 3 :
                math_new_data = self.new_data()
                print("\nOld Data \n",self.array)
                multiplictions = np.multiply(self.array,math_new_data)
                print("\nResult : \n",multiplictions)

            elif math_operation == 4 :
                math_new_data = self.new_data()
                print("\nOld Data : \n",self.array)
                divisions = np.divide(self.array,math_new_data)
                print("\nResult : \n",divisions)
            
            elif math_operation == 5 :
                print("\nExit the mathematical operation : \n")
                break

            else : 
                print ("Please Enter your choice Number in 1 to 5 : ")

    def combine_split (self):
        while True :
            print("\nChoose an option\n")
            print("1. Combine Arrays ")
            print("2. Split Array ")
            print("3. Exit \n")
            com_spt_choice = int(input("Enter your choice : "))

            if com_spt_choice == 1 :
                
                new_value = self.new_data()
                row_column = int(input("Enter the retrun value (vertical = 0 and horizontal = 1) : "))
                print("\nOld Data : \n",self.array)
                combine = np.concatenate((self.array,new_value), axis=row_column)
                print("\nCombined Array : \n",combine)

            elif com_spt_choice == 2 :

                split_num = int(input("Enter the split value number : "))
                row_column = int(input("Enter the retrun value (vertical = 0 and horizontal = 1) : "))

                print("Original Data : \n",self.array)
                split = np.split(self.array,[split_num],axis=row_column)
                print("\n Split Array : \n",split)

            elif com_spt_choice == 3 :
                print("Exit the combine and split . Thank you for visit. ")
                break

            else :
                print("Please Enter your choice number in (1 and 2) : ")
    

    def Search_sort_filter (self):
        while True:
            print("Choose an option : \n")
            print("1. Search : ")
            print("2. Sort : ")
            print("3. Filter : ")
            print("4. Go Back ")
            s_s_f_choice = int(input("Enter your choice :"))
            
            if s_s_f_choice == 1 :
                print("Choose an option : \n")
                print("1. Search the number : ")
                print("2. Search odd & even : ")
                print("3. Searchshored  the element index : ")
                choice_optn = int(input("\nEnter your choice :"))

                if choice_optn == 1 :
                    value_num = int(input("\nEnter the search element : "))
                    print("Original Array : \n",self.array)
                    a = np.where(self.array == value_num)
                    c = self.array[a]
                    print(f"{c},\n Total search element : {np.size(c)}")

                elif choice_optn == 2 :
                    value_num = int(input("\nSearch the data odd number(1) and even number (0) : "))
                    print("Original Array : \n",self.array)
                    sort = np.where(self.array%2 == value_num)
                    print(self.array[sort])
            
                elif choice_optn == 3:
                    value_num1 = int(input("\nEnter the search element index : "))
                    print("Original Array : \n",self.array)
                    
                    print("Choose the option : ")
                    print("1. right to left index..")
                    print("2. left to right index...")
                    choice_R_L = int(input("Enter your choice : "))

                    if choice_R_L == 1 :
                        dt = self.array
                        d1 = dt.flatten()

                        print (f"\nRight to left....\n,index number :-> {np.searchsorted(d1,value_num1,side='right')}")

                    elif choice_R_L == 2 :
                        dt = self.array
                        d1 = dt.flatten()
                        print (f"\nleft to right....\n, index number :-> {np.searchsorted(d1,value_num1,side='left')}")
                    else :
                        print("Enter your choice number in 1 and 2 : ")
                else : 
                    print("Enter your choice number in 1 to 3 : ")

            
            elif  s_s_f_choice == 2 :
                print("\nOriginal Array : \n",self.array)
                print("\nSort the Array : \n",np.sort(self.array))

            elif s_s_f_choice == 3 :
                print("Choose the option : ")
                print("1. Less Than (<) : ")
                print("2. Greater than (>) : ")
                print("3. odd & even :")
                filter_opn = int(input ("\nEnter your choice : "))

                if filter_opn == 1 :
                    print("\nOriginal array \n",self.array)
                    value_filter = int(input("\nEnter the less than element : "))
                    save_data = self.array < value_filter

                    newarray = self.array[save_data]
                    print(save_data)
                    print(newarray)

                elif filter_opn == 2 :
                    print("\nOriginal array \n",self.array)
                    value_filter = int(input("\nEnter the Greater than element : "))
                    save_data = self.array > value_filter

                    newarray = self.array[save_data]
                    print(save_data)
                    print(newarray)

                elif filter_opn == 3 :
                    print("\nOriginal array \n",self.array)
                    value_filter = int(input("\nEnter the odd number (1) and even number (0) : "))
                    save_data = self.array %2 == value_filter

                    newarray = self.array[save_data]
                    print(save_data)
                    print(newarray)

                else : 
                    print("Please Enter your choice number in 1 to 3 :")


            elif s_s_f_choice == 4 :
                print("Exit the Search , sort and filter operation : ")

                break

            else:
                print("Please Enter your choice number in 1 to 4 :")


            
    def Aggregates_Statistic (self):
        while True :
            print("\nChoose an Aggregate / statistical operation : \n")
            print("1. Sum : ")
            print("2. Mean : ")
            print("3. Median : ")
            print("4. Maximum : ")
            print("5. Standar Deviation : ")
            print("6. Variance : ")
            print("7. Exit : ")
            agg_stc_choice = int(input("Enter your choice : "))

            if agg_stc_choice == 1 :
                print("Array Sum :->  ",np.sum(self.array))
            
            elif agg_stc_choice == 2 :
                print("Array Mean :-> ",np.mean(self.array))

            elif agg_stc_choice == 3 :
                print("Array in  Median value:-> ",np.median(self.array))

            elif agg_stc_choice == 4 :
                print("Array in  Maximum value :-> ",np.max(self.array))

            elif agg_stc_choice == 5 :
                print("Array in Standar Deviation value :-> ",np.std(self.array))

            elif agg_stc_choice == 6:
                print("Array in variance :-> ",np.var(self.array))

            elif agg_stc_choice == 7 :
                print("Exit the Aggregates and Statistic operation : ")
                break

            else : 
                print("Please Enter your choice number in 1 to 7 :")

        

def Main ():

    


    while True :

        print("\n ============   Welcome to the Analzer project ========\n")

        print("choose an option : \n")
        print("1. Create a Numpy Array :")
        print("2. Indexing & clicing : ")
        print("3. Perform Mathematical operation : ")
        print("4. Combine or Split Array : ")
        print("5. Search , sort or Filter Arrays : ")
        print("6. Comput Aggregates and Statistics : ")
        print("7. Exit : ")
        choice = int(input ("\nEnter your choice : "))

        if choice == 1 :
            numpy_data = Numpy_array.Array_dimension()
            array_data = Numpy_array(numpy_data) 

        elif choice == 2 : 
            array_data.indexing_slicing()

        elif choice == 3 :
            array_data.Mathematical_Operation()

        elif choice == 4 :
            array_data.combine_split()

        elif choice == 5 :
            array_data.Search_sort_filter()
        
        elif choice == 6 :
            array_data.Aggregates_Statistic()

        elif choice == 7 :
            print("\nExit the Project ")
            print("")
            print("Thank you for using the Numpy Analyzer.! \n GOODBYE! \n")


Main()
       
