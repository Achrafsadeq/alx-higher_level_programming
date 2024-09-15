#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: Pointer to a Python object (must be a list)
 *
 * Description: This function takes a PyObject (expected to be a Python
 * list) and prints the size of the list, the allocated memory, and
 * the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);  /* Get size of the list */
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t i;
	/* Adding a blank line after declarations */
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
