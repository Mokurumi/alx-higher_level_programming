#include <Python.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a PyObject representing a list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, list_size = 0, allocated = 0;
	PyObject *item = NULL;
	char *item_type;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid PyListObject\n");
		return;
	}

	list_size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < list_size; ++i)
	{
		item = PyList_GetItem(p, i);
		if (item == NULL)
		{
			fprintf(stderr, "  [ERROR] Failed to get list item at index %ld\n", i);
			return;
		}

		item_type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, item_type);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a PyObject representing a bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, bytes_size = 0;
	const char *bytes_data = NULL;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid PyBytesObject\n");
		return;
	}

	bytes_size = PyBytes_Size(p);
	bytes_data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", bytes_data);
	printf("  first %ld bytes: ", bytes_size > 10 ? 10 : bytes_size);

	for (i = 0; i < bytes_size; ++i)
	{
		printf("%02x", (unsigned char)bytes_data[i]);
		if (i < bytes_size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a PyObject representing a float object
 */
void print_python_float(PyObject *p)
{
	double float_value = 0.0;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid PyFloatObject\n");
		return;
	}

	float_value = ((PyFloatObject *)p)->ob_fval;

	printf("[.] float object info\n");
	printf("  value: %f\n", float_value);
}
