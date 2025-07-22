/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

class SchoolDashboard extends Component {
    setup() {
        this.state = useState({ studentCount: 0,
                                teacherCount: 0,
                                institutions: [],
                                selectedInstitution: 0,
                                studentCount: 0,
                                classCount: 0,
                                sectionCount: 0});

        onWillStart(async () => {
            const result1 = await rpc("/school_dashboard/student_count", {});
            const result2 = await rpc("/school_dashboard/teacher_count", {});
            const institutionsResult = await rpc("/school_dashboard/institutions", {});
            this.state.studentCount = result1.count;
            this.state.teacherCount = result2.count;
            this.state.institutions = institutionsResult.institutions;
        });
    }
    async loadData() {
        const data = await rpc("/school_dashboard/institution_data", {
            institution_id: this.state.selectedInstitution || null,
        });
        this.state.studentCount = data.student_count;
        this.state.classCount = data.class_count;
        this.state.sectionCount = data.section_count;
    }

    async onInstitutionChange(ev) {
        this.state.selectedInstitution = parseInt(ev.target.value);
        await this.loadData();
    }
}

SchoolDashboard.template = "DashboardTemplate";

registry.category("actions").add("school_dashboard", SchoolDashboard);
