<template>
<div id="container">
  <div id="nav"></div>
  <div id="tasklist" :model="tasks">
    <el-row
    v-for="(task,index) in tasks"
    class="task-row row-bg"
    gutter="10"
    >
      <el-col clask="task-col" v-text="index+1" span="1"></el-col>
      <el-col clask="task-col" v-text="task.jira1" span="3"></el-col>
      <el-col clask="task-col" v-text="task.jira2" span="3"></el-col>
      <el-col clask="task-col" v-text="task.pkg" span="6"></el-col>
      <el-col clask="task-col" v-text="task.module" span="2"></el-col>
      <el-col clask="task-col" v-text="task.version" span="2"></el-col>
      <el-col clask="task-col" span="2"><el-switch class="task-col-status" v-model="task.status"></el-switch></el-col>
    </el-row>
  </div>
</div>
</template>

<script>
export default{
  data() {
    return {
      tasks: []
    }
  },
  load_tasks(){
    this.$axios.get('http://127.0.0.1:5000/api/tasks').then(function (response) {
      console.log(response);
      console.log(response.data);
      this.tasks = response.data;
    }).catch(function (error) {
      console.log(error);
    });
  }
}

</script>

<style>
body {
  overflow: scroll;
  font-size: 14px;
}

.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  };
  align: middle;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.task-col {
  height: 40px;
}
</style>