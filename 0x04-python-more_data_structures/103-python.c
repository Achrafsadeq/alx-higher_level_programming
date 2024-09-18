#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	const char *type_name;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		type_name = item->ob_type->tp_name;
		printf("Element %zd: %s\n", i, type_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;
	int max_bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	max_bytes = size > 10 ? 10 : (int)size;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %d bytes:", max_bytes + 1);

	for (i = 0; i <= max_bytes && i < size; i++)
	{
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}
