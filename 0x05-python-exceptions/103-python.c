#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * display_python_bytes_info - Displays details about a Python bytes object.
 * @py_obj: Pointer to a Python object, expected to be a bytes object.
 */
void display_python_bytes_info(PyObject *py_obj)
{
	char *byte_string;
	Py_ssize_t byte_size, idx;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(py_obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_string = PyBytes_AS_STRING(py_obj);
	byte_size = PyBytes_Size(py_obj);

	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", byte_string);

	Py_ssize_t display_size = byte_size >= 10 ? 10 : byte_size + 1;

	printf("  first %ld bytes: ", display_size);

	for (idx = 0; idx < display_size; idx++)
	{
		printf("%02hhx", byte_string[idx]);
		if (idx < display_size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * display_python_float_info - Displays details about a Python float object.
 * @py_obj: Pointer to a Python object, expected to be a float object.
 */
void display_python_float_info(PyObject *py_obj)
{
	char *float_str;
	double float_value;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(py_obj))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_value = PyFloat_AS_DOUBLE(py_obj);
	float_str = PyOS_double_to_string(float_value
			, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", float_str);
}

/**
 * display_python_list_info - Displays details about a Python list object.
 * @py_obj: Pointer to a Python object, expected to be a list object.
 */
void display_python_list_info(PyObject *py_obj)
{
	Py_ssize_t index, list_size;
	const char *element_type;
	PyListObject *list_obj;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(py_obj))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_obj = (PyListObject *)py_obj;
	list_size = PyList_GET_SIZE(py_obj);

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_obj->allocated);

	for (index = 0; index < list_size; index++)
	{
		element_type = (list_obj->ob_item[index])->ob_type->tp_name;
		printf("Element %ld: %s\n", index, element_type);

		if (strcmp(element_type, "bytes") == 0)
			display_python_bytes_info(list_obj->ob_item[index]);
		else if (strcmp(element_type, "float") == 0)
			display_python_float_info(list_obj->ob_item[index]);
	}
}
