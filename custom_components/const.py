"""Constants for the gzwater integration."""

DOMAIN = "gzwater"
CONF_USER_ID = "user_id"
CONF_PASSWORD = "password"
SCAN_INTERVAL = 86400  # 每天更新一次

# 传感器类型
SENSOR_TYPE_TOTAL_AMOUNT = "total_amount"
SENSOR_TYPE_USAGE = "usage"
SENSOR_TYPE_BILL_DATE = "bill_date"

SENSOR_TYPES = {
    SENSOR_TYPE_TOTAL_AMOUNT: {
        "name": "水费总额",
        "unit": "元",
        "icon": "mdi:water",
    },
    SENSOR_TYPE_USAGE: {
        "name": "用水量",
        "unit": "m³",
        "icon": "mdi:water-outline",
    },
    SENSOR_TYPE_BILL_DATE: {
        "name": "账单日期",
        "unit": "",
        "icon": "mdi:calendar",
    },
}