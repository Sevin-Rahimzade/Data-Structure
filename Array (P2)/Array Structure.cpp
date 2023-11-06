#include <iostream>
using namespace std;


class Array
{
private:
    int array[100];
    int temp = 0;

public:
    void append(int value)
    {
        this->array[this->temp] = value;
        temp++;
    }

    void insert(int value, int index)
    {
        for (int i = temp; i >= index; i--)
        {
            this->array[i + 1] = array[i];
        }
        this->array[index] = value;
        this->temp++;
    }
    
    int del(int index)
    {
        for (int i = index; i < temp; i++)
        {
            this->array[i] = array[i + 1];
        }
        temp--;
        return array[index];
    }    

    int find(int value)
    {
        for (int i = 0; i < temp - 1; i++)
        {
            if (value == array[i])
            {
                return i;
            }
        }
        return 0;
    }

    void display()
    {
        sort(this->array);
        for (int i = 0; i < temp; i++)
        {
            cout << array[i] << endl;
        }
    }

int main()
{
	Array array;
	array.display();
    return 0;
}
