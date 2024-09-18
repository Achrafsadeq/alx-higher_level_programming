#include <stdio.h>
#include <Python.h>

/**
 * display_python_bytes - Outputs details about a Python bytes object
 *
 * @p: Python object (expected to be of bytes type)
 * Return: Nothing is returned
 */
void display_python_bytes(PyObject *p)
{
	char *byte_str;
	long int length, i, boundary;

	printf("[.] Bytes object details\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	length = ((PyVarObject *)(p))->ob_size;
	byte_str = ((PyBytesObject *)p)->ob_sval;

	printf("  Size: %ld\n", length);
	printf("  Content: %s\n", byte_str);

	boundary = (length >= 10) ? 10 : length + 1;

	printf("  First %ld bytes:", boundary);

	for (i = 0; i < boundary; i++)
	{
		if (byte_str[i] >= 0)
			printf(" %02x", byte_str[i]);
		else
			printf(" %02x", 256 + byte_str[i]);
	}

	printf("\n");
}

/**
 * display_python_list - Outputs details about a Python list object
 *
 * @p: Python object (expected to be of list type)
 * Return: Nothing is returned
 */
void display_python_list(PyObject *p)
{
	long int length, i;
	PyListObject *list;
	PyObject *element;

	length = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list details\n");
	printf("[*] List length: %ld\n", length);
	printf("[*] Allocated memory: %ld\n", list->allocated);

	for (i = 0; i < length; i++)
	{
		element = list->ob_item[i];
		printf("Element %ld: %s\n", i, (element->ob_type)->tp_name);
		if (PyBytes_Check(element))
			display_python_bytes(element);
	}
}
