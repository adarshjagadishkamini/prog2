#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib();
	private:
		int age;
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
int Person::fib(){
	if (age <= 1) {
        return age; 
    } else {
        Person age_1(age - 1);
        Person age_2(age - 2);
        return age_1.fib() + age_2.fib(); //two objects created because the function doesn't take arguments
    }
}
		
	

void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}