<template> 
  <div id="init_tc">
    <el-select v-model="value2" placeholder="选择业务模块">
      <el-option
        v-for="item in options_module"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        :disabled="item.disabled">
      </el-option>
    </el-select>
    <el-select v-model="value2" placeholder="选择模板" style="margin-left: 20px;">
      <el-option
        v-for="item in options_template"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        :disabled="item.disabled">
      </el-option>
    </el-select>
    <el-row :gutter="20">
      <el-col :span="6">
        <el-input class="grid-content bg-purple" size="small" id="input_pkg" v-model="input" placeholder="输入专题名"></el-input>
      </el-col>
      <el-col :span="6">
        <el-input class="grid-content bg-purple" size="small" id="input_ver" v-model="input" placeholder="输入版本号">ver</el-input>
      </el-col>
      <el-col :span="6">
        <el-input class="grid-content bg-purple" size="small" id="input_title" v-model="input" placeholder="输入案例名"></el-input>
      </el-col>
      <el-col :span="6">
        <el-input class="grid-content bg-purple" size="small" id="input_description" v-model="input" placeholder="输入描述"></el-input>
      </el-col>
      <el-col :span="6">
        <el-input class="grid-content bg-purple" size="small" id="input_description" v-model="input" placeholder="输入案例名"></el-input>
      </el-col>
    </el-row>
  </div>
</template> 

<script>
  export default {
    data(){
      return {
        options_module: [{
          value: '0',
          label: '融资融券交易'
        }, {
          value: '1',
          label: '融资融券管理',        
        }, {
          value: '2',
          label: '信用创新业务'
        }],
        options_template: [{
          value: '0',
          label: '柜台'
        }, {
          value: '1',
          label: 'testapp',       
        }],
        value2: '',
        input: ''
      }
    }
  }
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
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
</style>
