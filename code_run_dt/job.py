from enum import Enum
from typing import Optional, Any, Literal

from pydantic import BaseModel, Field

__all__ = ["CodeRunJob", "CodeRunState", "JobRunState"]


class CodeRunJob(BaseModel):
    job_id: str = Field(..., title="任务ID")
    lang: Literal["c", "c++", "python", "rust"] = Field(
        "c", title="编程语言", description="code 使用的编程语言"
    )
    code: str = Field(..., title="代码")
    args: str = Field(..., title="参数")
    stdin: str = Field(..., title="标准输入")
    # run_config 里面的配置
    config: Optional[Any] = Field(None, title="运行配置")


class JobRunState(str, Enum):
    COMPILE_START = "compile_start"
    COMPILE_DONE = "compile_done"

    RUN_START = "run_start"
    RUN_DONE = "run_done"

    F_COMPILE = "f_compile"
    F_RUN = "f_run"
    F_SUCCESS = "f_success"


class CodeRunState(BaseModel):
    job_id: str = Field(..., title="任务ID")
    state: JobRunState = Field(..., title="任务状态")
    stdout: str = Field("", title="标准输出")
    stderr: str = Field("", title="标准错误")
