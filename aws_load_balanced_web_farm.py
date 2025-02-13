#!/usr/bin/env python3
#  coding=utf-8
#  vim:ts=4:sts=4:sw=4:et
#  pylint: disable=W0106
#
#  Author: Nho Luong
#  Date: 2023-04-14 13:54:52 +0100 (Fri, 14 Apr 2023)
#
#  https://github.com/nholuongut/diagrams-as-code
#
#  License: see accompanying Nho Luong LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn
#  and optionally send me feedback to help steer this or other code I publish
#
#  https://www.linkedin.com/in/nholuong
#

"""

AWS Load Balanced Web Farm

"""

# based on https://diagrams.mingrammer.com/docs/getting-started/examples

__author__ = 'Hari Sekhon'
__version__ = '0.3'

import os
from diagrams import Diagram

# ============================================================================ #
# AWS resources:
#
#   https://diagrams.mingrammer.com/docs/nodes/aws
#
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.onprem.client import Users

graph_attr = {
    "splines": "spline",
}

with Diagram("AWS Load Balanced Web Farm",
             show=not bool(os.environ.get('CI', 0)),
             direction="TB",
             filename='images/aws_load_balanced_web_farm',
             graph_attr=graph_attr,
             ):
    # can use variables to connect nodes to the same items
    # lb = ELB("lb")
    # db = RDS("events")
    # lb >> EC2("worker1") >> db
    # lb >> EC2("worker2") >> db
    # lb >> EC2("worker3") >> db
    # lb >> EC2("worker4") >> db
    # lb >> EC2("worker5") >> db

    elb = ELB("ELB\nElastic Load Balancer")

    Users('Users') >> elb

    # but less redundant code than the above can be achieved by grouping the workers into a list[]
    elb >> [EC2("Web Server 1"),
            EC2("Web Server 2"),
            EC2("Web Server 3"),
            EC2("Web Server 4"),
            EC2("Web Server 5")] >> RDS("RDS Database")
