<template> 
  <div id="app">
    <div id="nav">   
    </div>
    <div id="init_tc">     
      <el-row :gutter="10">
        <el-col :span="3">
          <el-autocomplete
            class="grid-content bg-purple" size="small" 
            v-model="state1"
            :fetch-suggestions="querySearch1"
            placeholder="选择业务模块"
            @select="handleSelect">
          </el-autocomplete>
        </el-col>
        <el-col :span="3">
          <el-autocomplete
            class="grid-content bg-purple" size="small" 
            v-model="state2"
            :fetch-suggestions="querySearch2"
            placeholder="选择模板"
            @select="handleSelect">
          </el-autocomplete>
          <el-button>生成</el-button>
        </el-col>
        <el-col :span="3">
          <el-date-picker
            v-model="value1"
            type="date"
            class="grid-content bg-purple" size="small"
            placeholder="选择日期">
          </el-date-picker>
        </el-col>
      </el-row>
      <el-row gutter="10">
        <el-col :span="3">
          <el-input class="grid-content bg-purple" size="small" id="input" v-model="input0" placeholder="输入专题名"></el-input>
        </el-col>
        <el-col :span="3">
          <el-input class="grid-content bg-purple" size="small" id="input" v-model="input1" placeholder="输入版本号">ver</el-input>
        </el-col>
        <el-col :span="3">
          <el-input class="grid-content bg-purple" size="small" id="input" v-model="input2" placeholder="输入案例名"></el-input>
        </el-col>
        <el-col :span="3">
          <el-input class="grid-content bg-purple" size="small" id="input" v-model="input3" placeholder="输入描述"></el-input>
        </el-col>
        <el-col :span="3">
          <el-input class="grid-content bg-purple" size="small" id="input" v-model="input4" placeholder="输入案例名"></el-input>
        </el-col>
      </el-row>
    </div>
  </div>
</template> 

<script>
  export default {
    data() {
      return {
        modules: [],
        templates: [],
        state1: '',
        state2: '',
        pickerOptions1: {
          disabledDate(time) {
            return time.getTime() > Date.now();
          },
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        },
        value1:''
      };
    },
    methods: {
      querySearch1(queryString, cb) {
        var modules = this.modules;
        var results0 = queryString ? modules.filter(this.createFilter0(queryString)) : modules;
        // 调用 callback 返回建议列表的数据
        cb(results0);
      },
      querySearch2(queryString, cb) {
        var templates = this.templates;
        var results1 = queryString ? templates.filter(this.createFilter1(queryString)) : templates;
        // 调用 callback 返回建议列表的数据
        cb(results1);
      },
      createFilter0(queryString) {
        return (module) => {
          return (module.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      createFilter1(queryString) {
        return (template) => {
          return (template.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      loadModules() {
        return [
          { "value": "融资融券交易" },
          { "value": "融资融券管理" },
          { "value": "股票质押" }
        ];
      },
      loadTemplates() {
        return [
          { "value": "柜台" },
          { "value": "testapp" }
        ];
      },
      handleSelect(item) {
        console.log(item);
      }
    },
    mounted() {
      this.modules = this.loadModules();
      this.templates = this.loadTemplates();
    }
  }
</script>

<style scoped>
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
<style>
body {
  overflow: hidden;
}
el-row {
  padding: 5px 0;
}
</style>