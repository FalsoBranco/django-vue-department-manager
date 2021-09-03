<template>
  <button
    type="button"
    class="btn btn-primary m-2 fload-end"
    data-bs-toggle="modal"
    data-bs-target="#exampleModal"
    @click="addClick()"
  >
    Add Employee
  </button>
  <table class="table table-striped">
    <thead>
      <tr>
        <td>Employee Id</td>
        <td>Employee Name</td>
        <td>Department</td>
        <td>Date Of Joining</td>
        <td>Options</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="employee in employees" :key="employee.id">
        <td>{{ employee.id }}</td>
        <td>{{ employee.name }}</td>
        <td>{{ employee.department }}</td>
        <td>{{ employee.date_of_joining }}</td>
        <td>
          <button
            type="button"
            class="btn btn-light mr-1"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            @click="editClick(employee)"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-pencil-square"
              viewBox="0 0 16 16"
            >
              <path
                d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
              />
              <path
                fill-rule="evenodd"
                d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
              />
            </svg>
          </button>
          <button
            class="btn btn-light mr-1"
            type="button"
            @click="deleteClick(employee.id)"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-trash-fill"
              viewBox="0 0 16 16"
            >
              <path
                d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"
              />
            </svg>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
  <div
    id="exampleModal"
    class="modal fade"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 id="exampleModalLabel" class="modal-title">{{ modalTitle }}</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="d-flex flex-row bd-highlight mb-3">
            <div class="p-2 w-50 bd-highlight">
              <div class="input-group mb-3">
                <span class="input-group-text">Name</span>
                <input
                  v-model="employee.name"
                  type="text"
                  class="form-control"
                />
              </div>
              <div class="input-group mb-3">
                <!-- <span class="input-group-text">Department</span>
                <select v-model="employee.department" class="form-select">
                  <option v-for="dep in departments" :key="dep">
                    {{ dep }}
                  </option>
                </select> -->
                <span class="input-group-text">Department</span>
                <input
                  v-model="employee.department"
                  type="text"
                  class="form-control"
                  list="departments"
                />
                <datalist id="departments">
                  <option v-for="dep in departments" :key="dep">
                    {{ dep }}
                  </option>
                </datalist>
              </div>
              <div class="input-group mb-3">
                <span class="input-group-text">DOJ</span>
                <input
                  v-model="employee.date_of_joining"
                  type="date"
                  class="form-control"
                />
              </div>
            </div>
          </div>
          <button
            v-if="employee.id == 0"
            type="button"
            class="btn btn-primary"
            @click="createClick()"
          >
            Create
          </button>
          <button
            v-if="employee.id != 0"
            class="btn btn-primary"
            type="button"
            @click="updateClick(employee.id)"
          >
            Update
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive, ref } from 'vue';
import EmployeeDataService from '../services/EmployeeDataservice.js';
import EmployeeDataservice from '../services/EmployeeDataservice.js';
export default {
  name: 'Employee',
  components: {},
  setup() {
    const departments = ref([]);
    const modalTitle = ref('');
    const employees = ref([]);
    const employee = reactive({
      id: 0,
      name: '',
      department: '',
      date_of_joining: '',
    });

    const addClick = () => {
      modalTitle.value = 'Add Employee';
      employee.id = 0;
      employee.name = '';
      employee.department = '';
      employee.date_of_joining = '';
    };
    const createClick = () => {
      EmployeeDataservice.create(employee)
        .then((response) => {
          employees.value.push(response.data);
        })
        .catch((e) => console.log(e));
    };

    const editClick = (emp) => {
      employee.id = emp.id;
      employee.name = emp.name;
      employee.department = emp.department;
      employee.date_of_joining = emp.date_of_joining;
    };
    const updateClick = (id) => {
      EmployeeDataservice.update(id, employee)
        .then((response) => {
          const updatedEmployee = employees.value.findIndex(
            (item) => item.id === id
          );

          employees.value[updatedEmployee] = employee;
        })
        .catch((e) => console.log(e));
    };
    const deleteClick = (id) => {
      EmployeeDataService.delete(id)
        .then((response) => {
          const deletedEmployeeIndex = employees.value.findIndex(
            (item) => item.id === id
          );
          employees.value.splice(deletedEmployeeIndex, 1);
        })
        .catch((e) => {
          console.log(e);
        });
    };

    onMounted(() => {
      EmployeeDataService.getAll()
        .then((response) => {
          employees.value = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
      EmployeeDataService.getDepartments()
        .then((response) => {
          departments.value = response.data.data;
        })
        .catch((e) => {
          console.log(e);
        });
    });
    return {
      modalTitle,
      employees,
      employee,
      departments,

      editClick,
      updateClick,
      deleteClick,
      addClick,
      createClick,
    };
  },
};
</script>

<style></style>
