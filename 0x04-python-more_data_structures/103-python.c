#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Outputs information about Python byte objects.
 *
 * @p: Python object to be analyzed.
 * Return: Nothing is returned from this function.
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, index, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  attempting to print string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (index = 0; index < limit; index++)
		if (string[index] >= 0)
			printf(" %02x", string[index]);
		else
			printf(" %02x", 256 + string[index]);

	printf("\n");
}

/**
 * print_python_list - Displays details of a Python list object.
 *
 * @p: Python object (list) to inspect.
 * Return: No value is returned.
 */
void print_python_list(PyObject *p)
{
	long int size, index;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Total size of the Python List = %ld\n", size);
	printf("[*] Memory allocated = %ld\n", list->allocated);

	for (index = 0; index < size; index++)
	{
		obj = ((PyListObject *)p)->ob_item[index];
		printf("Element %ld: %s\n", index, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
