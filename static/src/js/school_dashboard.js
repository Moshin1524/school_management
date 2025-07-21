/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

class SchoolDashboard extends Component {
    setup() {
        this.state = useState({ studentCount: 0, teacherCount: 0 });

        onWillStart(async () => {
            const result1 = await rpc("/school_dashboard/student_count", {});
            const result2 = await rpc("/school_dashboard/teacher_count", {});
            this.state.studentCount = result1.count;
            this.state.teacherCount = result2.count;
        });
    }
}

SchoolDashboard.template = "DashboardTemplate";

registry.category("actions").add("school_dashboard", SchoolDashboard);
