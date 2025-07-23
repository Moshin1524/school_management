import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

class CustomDashboard extends Component {
    setup() {
        this.state = useState({
        institutions: [],
        selectedInstitution: null,
        studentCount: 0,
        teacherCount: 0,
        classCount: 0,
        sectionCount: 0,});

    onWillStart(async () => {
        // Load institutions
        this.state.institutions = await rpc("/web/dataset/call_kw", {
        model: "school.dashboard.data",
        method: "get_institutions",
        args: [],
        kwargs: {},});});
    }
    async onInstitutionChange(ev) {
            const institutionId = parseInt(ev.target.value);
            this.state.selectedInstitution = institutionId || null;

            const counts = await rpc("/web/dataset/call_kw", {
            model: "school.dashboard.data",
            method: "get_dashboard_counts",
            args: [],
            kwargs: { institution_id: institutionId },
        });

        this.state.studentCount = counts.student_count;
        this.state.teacherCount = counts.teacher_count;
        this.state.classCount = counts.class_count;
        this.state.sectionCount = counts.section_count;
    }

}

CustomDashboard.template = "CustomDashboardTemplate";
CustomDashboard.props = {};
registry.category("actions").add("custom_dashboard", CustomDashboard);
