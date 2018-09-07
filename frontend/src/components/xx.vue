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
    <br>
    <el-select v-model="value2" placeholder="选择模板">
      <el-option
        v-for="item in options_template"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        :disabled="item.disabled">
      </el-option>
    </el-select>
    <el-input size="small" id="input_pkg" v-model="input" placeholder="输入专题名"></el-input>
    <el-input size="small" id="input_ver" v-model="input" placeholder="输入版本号">ver</el-input>
    <el-input size="small" id="input_title" v-model="input" placeholder="输入案例名"></el-input>
    <el-input size="small" id="input_author" v-model="input" placeholder="输入作者"></el-input>
    <el-input size="small" id="input_description" v-model="input" placeholder="输入描述"></el-input>
    <el-input size="small" id="input_script" v-model="input" placeholder="关联脚本"></el-input>
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
</style>
