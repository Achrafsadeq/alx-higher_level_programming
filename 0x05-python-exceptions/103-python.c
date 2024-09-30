#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - Displays information about Python byte objects
 * @p: PyObject pointer that should be a byte object
 *
 * This function checks if the provided object is a valid
 * Python byte object, and if so, prints details such as its size,
 * string content, and up to the first 10 bytes in hexadecimal format.
 * If the object is not a byte object, it prints an error message.
 */
void print_python_bytes(PyObject *p)
{
	size_t byte_count, index;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = ((PyBytesObject *)(p))->ob_sval;
	byte_count = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", byte_count, str);
	byte_count >= 10 ? byte_count = 10 : byte_count++;
	printf("  first %ld bytes: ", byte_count);
	for (index = 0; index < byte_count - 1; index++)
		printf("%02hhx ", str[index]);
	printf("%02hhx\n", str[index]);
}

/**
 * print_python_float - Displays details of Python float objects
 * @p: PyObject pointer expected to be a float
 *
 * This function checks if the passed object is a Python float
 * and if valid, it prints the float value. If the object is
 * not a float, an error message is shown.
 */
void print_python_float(PyObject *p)
{
	char *str;
	double float_value;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	float_value = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_list - Prints information about Python list objects
 * @p: PyObject pointer expected to be a list
 *
 * The function verifies whether the input is a valid Python list.
 * If so, it displays the list's size, allocated memory, and the
 * type of each element within the list. Special handling is done
 * for bytes and float elements, with additional details printed
 * for those types.
 */
void print_python_list(PyObject *p)
{
	size_t allocated, list_size, element_index;
	const char *element_type;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	list_size = PyList_GET_SIZE(p);
	allocated = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n",
			list_size, allocated);
	for (element_index = 0; element_index < list_size; element_index++)
	{
		element_type = (list->ob_item[element_index])->ob_type->tp_name;
		printf("Element %li: %s\n", element_index, element_type);
		!strcmp(element_type, "bytes") ?
			print_python_bytes(list->ob_item[element_index]) : (void)element_type;
		!strcmp(element_type, "float") ?
			print_python_float(list->ob_item[element_index]) : (void)element_type;
	}
}
