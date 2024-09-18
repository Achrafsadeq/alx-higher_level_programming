#include <stdio.h>
#include <Python.h>

/**
 * display_python_bytes - Displays details about a bytes object
 *
 * @p: Python object to inspect
 * Description: Outputs essential information about the bytes object,
 * including size, contents, and the first few bytes in hexadecimal.
 * Return: Nothing (void function)
 */
void display_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	printf("[.] Bytes object details\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Not a valid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  Size: %ld\n", size);
	printf("  String content: %s\n", string);

	limit = (size >= 10) ? 10 : size + 1;

	printf("  First %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * display_python_list - Displays details about a Python list
 *
 * @p: Python object to inspect
 * Description: Provides information about the size, elements, and memory
 * allocation of a Python list, and also handles byte objects within the list.
 * Return: Nothing (void function)
 */
void display_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list details\n");
	printf("[*] Python List Size = %ld\n", size);
	printf("[*] Memory allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			display_python_bytes(obj);
	}
}
