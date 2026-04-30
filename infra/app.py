#!/usr/bin/env python3

import aws_cdk as cdk

from stacks.frontend_stack import FrontendStack

app = cdk.App()

FrontendStack(
    app,
    "GradingCloudWebFrontendStack",
)

app.synth()
