from oracle50empleados import OracleEmpleados
oracle = OracleEmpleados()
print("Delete empleados clases")
print("Dame un Id de empleado")
empno = int(input())
reg = oracle.eliminarEmpleado(empno)
print(f"Empleados eliminados: {reg}")
print("Fin de programa")