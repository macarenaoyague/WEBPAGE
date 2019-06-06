$(function(){
    var url = "http://0.0.0.0:8080/subjects";
    var urlCareers = "http://0.0.0.0:8080/careers";

    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "id",
            loadUrl: url ,
            insertUrl: url ,
            updateUrl: url ,
            deleteUrl: url ,
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: true };
            }
        }),
        editing: {
            allowUpdating: true,
            allowDeleting: true,
            allowAdding: true
        },
        remoteOperations: {
            sorting: true,
            paging: true
        },
        paging: {
            pageSize: 12
        },
        pager: {
            showPageSizeSelector: true,
            allowedPageSizes: [8, 12, 20]
        },
        columns: [{
            dataField: "id_subject",
            dataType: "number",
            allowEditing: false
        }, {
            dataField: "name_subject",
        }, {
            dataField: "career_from_id",
            dataType: "number",
            lookup: {
                dataSource: DevExpress.data.AspNet.createStore({
                    key: "id",
                    loadUrl: urlCareers,
                    onBeforeSend: function(method, ajaxOptions) {
                        ajaxOptions.xhrFields = { withCredentials: true };
                    }
                }),
                valueExpr: "id",
                displayExpr: "name_career"
            }
        },  ],
    }).dxDataGrid("instance");
});
