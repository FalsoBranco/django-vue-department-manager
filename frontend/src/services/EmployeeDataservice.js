import http from '../http_commons';

class EmployeeDataService {
  create(data) {
    return http.post('/employee', data);
  }
  getAll() {
    return http.get('/employee');
  }
  getDepartments() {
    return http.get('/employee/departments');
  }
  delete(id) {
    return http.delete(`/employee/${id}`);
  }
  update(id, data) {
    return http.put(`/employee/${id}`, data);
  }
}

export default new EmployeeDataService();
