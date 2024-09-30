#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);
/**
 * display_python_bytes - Outputs information about a Python bytes object.
 * @p: Pointer to the PyObject representing the bytes.
 */
void print_python_bytes(PyObject *p)
{
    size_t b, index;
    char *str;

    setbuf(stdout, NULL);
    printf("[.] bytes object details\n");
    if (PyBytes_Check(p) == 0)
    {
        printf("  [ERROR] Not a valid Bytes Object\n");
        return;
    }
    str = ((PyBytesObject *)(p))->ob_sval, b = PyBytes_Size(p);
    printf("  size: %ld\n  attempting string: %s\n", b, str);
    b >= 10 ? b = 10 : b++;
    printf("  first %ld bytes: ", b);
    for (index = 0; index < b - 1; index++)
        printf("%02hhx ", str[index]);
    printf("%02hhx\n", str[index]);
}

/**
 * display_python_float - Outputs details about a Python float object.
 * @p: Pointer to the PyObject representing the float.
 */
void print_python_float(PyObject *p)
{
    char *str;
    double f;

    setbuf(stdout, NULL);
    printf("[.] float object details\n");
    if (PyFloat_Check(p) == 0)
    {
        printf("  [ERROR] Not a valid Float Object\n");
        return;
    }
    f = ((PyFloatObject *)(p))->ob_fval;
    str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str);
}

/**
 * display_python_list - Outputs information about a Python list object.
 * @p: Pointer to the PyObject representing the list.
 */
void print_python_list(PyObject *p)
{
    size_t a, size, index;
    const char *t;
    PyListObject *list;

    setbuf(stdout, NULL);
    printf("[*] Python list details\n");
    if (PyList_Check(p) == 0)
    {
        printf("  [ERROR] Not a valid List Object\n");
        return;
    }
    list = (PyListObject *)p;
    size = PyList_GET_SIZE(p);
    a = list->allocated;
    printf("[*] Number of elements in the Python List = %ld\n[*] Allocated space = %li\n", size, a);
    for (index = 0; index < size; index++)
    {
        t = (list->ob_item[index])->ob_type->tp_name;
        printf("Element %li: %s\n", index, t);
        !strcmp(t, "bytes") ? print_python_bytes(list->ob_item[index]) : (void)t;
        !strcmp(t, "float") ? print_python_float(list->ob_item[index]) : (void)t;
    }
}

