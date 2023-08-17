#include <Python.h>

/**
 * print_python_list - print py list
 *
 * @p: py object input
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_size, alloc_size, i;
	PyObject *item;
	const char *item_type;

	if (PyList_Check(p))
	{
		list_size = PyList_Size(p);
		alloc_size = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", alloc_size);

		for (i = 0; i < list_size; ++i)
		{
			item = PyList_GetItem(p, i);
			item_type = item->ob_type->tp_name;
			printf("Element %ld: %s\n", i, item_type);
		}
	}
	else
	{
		fprintf(stderr, "Invalid Python List Object\n");
	}
}

/**
 * print_python_bytes - print py list
 *
 * @p: py object input
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, i;
	const char *bytes_data;

	if (PyBytes_Check(p))
	{
		bytes_size = PyBytes_Size(p);
		bytes_data = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  Size: %ld\n", bytes_size);
		printf("  Trying string: %s\n", bytes_data);
		printf("  first %ld bytes: ", bytes_size + 1 > 10 ? 10 : bytes_size + 1);
		for (i = 0; i < bytes_size + 1 && i < 10; ++i)
		{
			printf("%02hhx", bytes_data[i]);
			if (i + 1 < 10 && i + 1 < bytes_size + 1)
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	else
	{
		fprintf(stderr, "Invalid Python Bytes Object\n");
	}
}
