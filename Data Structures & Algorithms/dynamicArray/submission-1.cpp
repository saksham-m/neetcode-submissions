class DynamicArray {
private:
    int *arr;
    int cap;
    int size;
public:

    DynamicArray(int capacity) {
        arr = (int*)malloc(cap* sizeof(int));
        cap = capacity;
        size = 0;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == cap){
            resize();
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        int val = arr[size-1];
        size--;
        return val;
    }

    void resize() {
        arr = (int*)realloc(arr, 2*cap*sizeof(int));
        cap *=2;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return cap;
    }
};
