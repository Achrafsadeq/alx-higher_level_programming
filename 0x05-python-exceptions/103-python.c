#include <Python.h>
#include <stdio.h>

/**
 * display_python_list_info - Shows details of a Python list object
 * @py_list: Pointer to a Python object (expected to be a PyListObject)
 *
 * This function prints information about a Python list, including its size,
 * allocated memory, and details about each element.
 */
void display_python_list_info(PyObject *py_list)
{
	Py_ssize_t list_size, mem_allocated, index;
	PyObject *element;
	const char *type_name;

	if (!PyList_Check(py_list))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	list_size = PyList_GET_SIZE(py_list);
	mem_allocated = ((PyListObject *)py_list)->allocated;

	printf("[*] Python list info\n");
	printf("[*] List size = %zd\n", list_size);
	printf("[*] Memory allocated = %zd\n", mem_allocated);

	for (index = 0; index < list_size; ++index)
	{
		element = PyList_GET_ITEM(py_list, index);
		type_name = Py_TYPE(element)->tp_name;
		printf("Item %zd: %s\n", index, type_name);

		if (PyBytes_Check(element))
			display_python_bytes_info(element);
		else if (PyFloat_Check(element))
			display_python_float_info(element);
	}
}

/**
 * display_python_bytes_info - Shows details of a Python bytes object
 * @py_bytes: Pointer to a Python object (expected to be a PyBytesObject)
 *
 * This function prints information about a Python bytes object, including its
 * size, string representation, and the first few bytes in hexadecimal.
 */
void display_python_bytes_info(PyObject *py_bytes)
{
	Py_ssize_t byte_count, display_limit, i;
	char *byte_data;

	if (!PyBytes_Check(py_bytes))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_count = PyBytes_GET_SIZE(py_bytes);
	byte_data = PyBytes_AS_STRING(py_bytes);
	display_limit = (byte_count < 10) ? byte_count : 10;

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", byte_count);
	printf("  trying string: %s\n", byte_data);
	printf("  first %zd bytes:", display_limit);

	for (i = 0; i < display_limit; ++i)
		printf(" %02hhx", byte_data[i]);

	printf("\n");
}

/**
 * display_python_float_info - Shows details of a Python float object
 * @py_float: Pointer to a Python object (expected to be a PyFloatObject)
 *
 * This function prints the value of a Python float object.
 */
void display_python_float_info(PyObject *py_float)
{
	double float_value;

	if (!PyFloat_Check(py_float))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	float_value = PyFloat_AS_DOUBLE(py_float);

	printf("[.] float object info\n");
	printf("  value: %g\n", float_value);
}
